if !exists('g:loaded_lspsaga') | finish | endif

lua << EOF
local saga = require 'lspsaga'

saga.init_lsp_saga {
  error_sign = '',
  warn_sign = '',
  hint_sign = '',
  infor_sign = '',
  border_style = "round",
  finder_definition_icon = '  ',
  finder_reference_icon = '  ',
}

EOF

nnoremap <silent> <C-j> :Lspsaga diagnostic_jump_next<CR>
" show hover doc
nnoremap <silent>K :Lspsaga hover_doc<CR>
inoremap <silent> <C-k> <Cmd>Lspsaga signature_help<CR>
"nnoremap <silent> K <cmd>lua require('lspsaga.hover').render_hover_doc()<CR>
nnoremap <silent> gh :Lspsaga lsp_finder<CR>
nnoremap <silent> gp :Lspsaga preview_definition<CR>

nnoremap <silent><C-Space> :Lspsaga code_action<CR>
vnoremap <silent><C-Space> :<C-U>Lspsaga range_code_action<CR>
