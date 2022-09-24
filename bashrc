#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias pacman='pacman --color=auto'
alias grep='grep --color=auto'
alias ls='lsd'

GREEN="\[$(tput setaf 2)\]"
BLUE="\[$(tput setaf 4)\]"
RESET="\[$(tput sgr0)\]"
PS1="${BLUE}\w ${GREEN}> ${RESET}"
export VISUAL=/usr/bin/nvim

set -o vi
