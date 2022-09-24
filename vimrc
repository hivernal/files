set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

Plugin 'ycm-core/YouCompleteMe'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'

Plugin 'jiangmiao/auto-pairs'
Plugin 'matze/vim-move'
Plugin 'itchyny/lightline.vim'
Plugin 'tpope/vim-surround'

Plugin 'tomasr/molokai'
call vundle#end()
filetype plugin indent on

"colorscheme
let g:molokai_original = 1
set background=dark
colo molokai
if (empty($TMUX))
  if (has("nvim"))
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  if (has("termguicolors"))
    set termguicolors
  endif
endif

"lightline
set noshowmode
set laststatus=2

"general
syntax on
set relativenumber
set mouse=a
set number
set cursorline

set visualbell
set hidden

set tabstop=4
set shiftwidth=4
set expandtab
set smarttab
set lazyredraw
set smartindent
set autoindent

set showcmd
set noswapfile
set ruler
let mapleader = ','
set encoding=utf-8
set backspace=indent,eol,start
set history=500
set wrap

"vimspector
"let g:vimspector_enable_mappings = 'HUMAN'
"packadd! vimspector

"Move
let g:move_key_modifier = 'c'

"Files
nmap <Leader>f :tabn<cr>
nmap  <Leader>d :tabp<cr>
nmap  <Leader>s :tabe
nmap  <c-s> :wa<cr>

"ultisnips
let g:UltiSnipsExpandTrigger="<c-l>"
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-k>"

"You Complete Me
set completeopt-=preview
let g:ycm_min_num_of_chars_for_completion = 1
let g:ycm_max_num_candidates = 20
let g:ycm_clangd_uses_ycmd_caching = 0
let g:ycm_clangd_binary_path = exepath("clangd")
