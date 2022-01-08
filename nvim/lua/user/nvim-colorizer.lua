
-- Setup nvim-cmp.
local status_ok, ncolorizer = pcall(require, "colorizer")
if not status_ok then
  return
end

ncolorizer.setup {
 'css';
 'javascript';
 'typescript';
 html = {
   mode = 'foreground';
 }
}

