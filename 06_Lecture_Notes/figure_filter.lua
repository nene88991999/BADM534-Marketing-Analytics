-- Keep Markdown readable on GitHub; use editable vector TikZ in the PDF.
function Para(el)
  if #el.content == 1 and el.content[1].t == 'Image' then
    local img = el.content[1]
    local name = img.src:match('figures/(.-)%.png$')
    if name then
      local caption = pandoc.utils.stringify(img.caption):gsub('%%','\\%%'):gsub('&','\\&'):gsub('_','\\_')
      return pandoc.RawBlock('latex', '\\begin{figure}[htbp]\n\\centering\n\\input{figures/'..name..'.tex}\n\\caption{'..caption..'}\\label{fig:'..name..'}\n\\end{figure}')
    end
  end
end
function Header(el)
  local prefix = PANDOC_STATE.input_files[1]:match("(M%d+)_") or "module"
  el.identifier = prefix .. "-" .. el.identifier
  -- LaTeX supplies chapter and section numbers; retain M1-M8 in Markdown.
  if el.content[1] and el.content[1].t == 'Str' then
    local s = el.content[1].text
    if s:match('^M%d+%.$') or s:match('^%d+%.%d+$') then
      table.remove(el.content, 1)
      if el.content[1] and el.content[1].t == 'Space' then table.remove(el.content, 1) end
    end
  end
  return {el, pandoc.RawBlock('latex','\\noindent')}
end
function Link(el)
  -- Module sources are one directory deeper than the assembled PDF.
  if el.target:match('^%.%./%.%./') then
    el.target = el.target:gsub('^%.%./%.%./','../')
  end
  return el
end

function Table(el)
  -- Pandoc 2.12 rounds LaTeX column proportions to two decimals. Ensure
  -- those rounded proportions sum to one, preventing table overflow.
  local total = 0
  for _, spec in ipairs(el.colspecs) do total = total + (spec[2] or 0) end
  if total > 0 then
    local assigned = 0
    for i, spec in ipairs(el.colspecs) do
      local percent
      if i == #el.colspecs then percent = 100 - assigned
      else percent = math.floor(100 * (spec[2] or 0) / total) end
      spec[2] = percent / 100
      assigned = assigned + percent
    end
  end
  return el
end
