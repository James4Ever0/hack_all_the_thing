cat apt_export_termux.log | fzf | xargs -iabc grep -C 3 "abc" apt_export_termux.log
