cat apt_export_termux.log | fzf | xargs -iabc grep -C 3 "abc" apt_export_termux.log

# you can develop a processor to add similar words dynamically per line, then remove these words at the end of search
