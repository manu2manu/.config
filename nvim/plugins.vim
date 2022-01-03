" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')
"========================================================
"  Themes
"========================================================

Plug 'morhetz/gruvbox'

Plug 'preservim/nerdtree'
Plug 'jistr/vim-nerdtree-tabs'
" For Git
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'
" gitsigns
Plug 'lewis6991/gitsigns.nvim'
Plug 'nvim-lua/plenary.nvim'
" Auto close (), {}, ""
Plug 'cohama/lexima.vim'

if has('nvim')
  Plug 'hoob3rt/lualine.nvim'
  Plug 'kristijanhusak/defx-git'
  Plug 'kristijanhusak/defx-icons'
  Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' }
  Plug 'neovim/nvim-lspconfig'
  Plug 'glepnir/lspsaga.nvim'
  Plug 'kosayoda/nvim-lightbulb'
  Plug 'folke/lsp-colors.nvim'
  Plug 'L3MON4D3/LuaSnip'
  Plug 'hrsh7th/cmp-nvim-lsp'
  Plug 'hrsh7th/cmp-buffer'
  Plug 'hrsh7th/nvim-cmp'
  Plug 'nvim-treesitter/nvim-treesitter', { 'do': ':TSUpdate' }
  Plug 'kyazdani42/nvim-web-devicons'
  Plug 'onsails/lspkind-nvim'
  Plug 'nvim-lua/popup.nvim'
  Plug 'nvim-lua/plenary.nvim'
  Plug 'nvim-telescope/telescope.nvim'
  Plug 'windwp/nvim-autopairs'
  Plug 'norcalli/nvim-colorizer.lua'
endif

Plug 'groenewege/vim-less', { 'for': 'less' }
call plug#end()
