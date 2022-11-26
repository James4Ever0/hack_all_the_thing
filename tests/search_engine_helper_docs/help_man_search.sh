man $1 | fzf | xargs -iabc bash -c 'man '$1' | grep -C 5 "abc"'
