cat apt_export_termux.log | fzf -d 3 | xargs -iabc grep -C 3 "abc" apt_export_termux.log
