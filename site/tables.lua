-- The per-subset guide is a four-column table with long cells.  It is marked so the stylesheet can give its
-- columns their own minimum widths, and every <br>-separated item of a cell becomes a paragraph of its own.
local function split_breaks(blocks)
  local out = {}
  for _, block in ipairs(blocks) do
    if block.t == "Plain" or block.t == "Para" then
      local current = {}
      for _, inline in ipairs(block.content) do
        local is_break = inline.t == "LineBreak"
          or (inline.t == "RawInline" and inline.text:match("^<br%s*/?>$") ~= nil)
        if is_break then
          if #current > 0 then out[#out + 1] = pandoc.Para(current) end
          current = {}
        else
          current[#current + 1] = inline
        end
      end
      if #current > 0 then out[#out + 1] = pandoc.Para(current) end
    else
      out[#out + 1] = block
    end
  end
  return out
end

-- Every table: mark each cell with a width class taken from the longest cell of its column, so the stylesheet
-- can keep columns readable (a table that does not fit scrolls sideways instead of being squeezed), and
-- wrap the table in a scrolling box.
local function width_class(n)
  if n <= 14 then return "c-num" end
  if n <= 40 then return "c-s" end
  if n <= 110 then return "c-m" end
  if n <= 260 then return "c-l" end
  return "c-xl"
end

function Table(t)
  local longest = {}
  for _, body in ipairs(t.bodies) do
    for _, row in ipairs(body.body) do
      for i, cell in ipairs(row.cells) do
        local n = pandoc.utils.stringify(cell.contents):len()
        if not longest[i] or n > longest[i] then longest[i] = n end
      end
    end
  end
  local function mark(rows)
    for _, row in ipairs(rows) do
      for i, cell in ipairs(row.cells) do
        cell.attr.classes:insert(width_class(longest[i] or 0))
      end
    end
  end
  mark(t.head.rows)
  for _, body in ipairs(t.bodies) do mark(body.body) end

  local head = ""
  for _, row in ipairs(t.head.rows) do
    for _, cell in ipairs(row.cells) do
      head = head .. pandoc.utils.stringify(cell.contents) .. "|"
    end
  end
  local classes = { "tablewrap" }
  if head:find("How it finishes", 1, true) then
    for _, body in ipairs(t.bodies) do
      for _, row in ipairs(body.body) do
        for _, cell in ipairs(row.cells) do
          cell.contents = split_breaks(cell.contents)
        end
      end
    end
    classes[#classes + 1] = "guide"
  end
  return pandoc.Div({ t }, pandoc.Attr("", classes))
end
