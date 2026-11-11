-- The per-subset guide is a four-column table with long cells.  Mark it so the stylesheet can give its
-- columns sensible minimum widths (otherwise the browser squeezes the second column to one word), and
-- turn every <br>-separated item of a cell into a paragraph of its own.
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

function Table(t)
  local head = ""
  for _, row in ipairs(t.head.rows) do
    for _, cell in ipairs(row.cells) do
      head = head .. pandoc.utils.stringify(cell.contents) .. "|"
    end
  end
  if head:find("How it finishes", 1, true) then
    for _, body in ipairs(t.bodies) do
      for _, row in ipairs(body.body) do
        for _, cell in ipairs(row.cells) do
          cell.contents = split_breaks(cell.contents)
        end
      end
    end
    return pandoc.Div({ t }, pandoc.Attr("", { "guide" }))
  end
end
