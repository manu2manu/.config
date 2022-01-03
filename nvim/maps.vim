let mapleader=" "

"========================================================
" Tabs navigation
"========================================================
" TAB in general mode will move to text buffer
 nnoremap <TAB> :bnext<CR>
" SHIFT-TAB will go back
 nnoremap <S-TAB> :bprevious<CR>

" Select all 
nmap <C-a> gg<S-v>G

" Increment/decrement
nnoremap + <C-a>
nnoremap - <C-x>

"------------------------------
" Windows

" Split window
nmap ss :split<Return><C-w>w
nmap sv :vsplit<Return><C-w>w

" Move window
nmap <Space> <C-w>w
map s<left> <C-w>h
map s<up> <C-w>k
map s<down> <C-w>j
map s<right> <C-w>l
map sh <C-w>h
map sk <C-w>k
map sj <C-w>j
map sl <C-w>l
" Resize window
nmap <C-w><left> <C-w><
nmap <C-w><right> <C-w>>
nmap <C-w><up> <C-w>+
nmap <C-w><down> <C-w>-
