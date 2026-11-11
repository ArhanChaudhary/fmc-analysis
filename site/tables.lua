-- The per-subset guide is a four-column table with long cells.  Mark it so the stylesheet can give its
-- columns sensible minimum widths (otherwise the browser squeezes the second column to one word).
function Table(t)
  local head = ""
  for _, row in ipairs(t.head.rows) do
    for _, cell in ipairs(row.cells) do
      head = head .. pandoc.utils.stringify(cell.contents) .. "|"
    end
  end
  if head:find("How it finishes", 1, true) then
    return pandoc.Div({ t }, pandoc.Attr("", { "guide" }))
  end
end
