cat ffmpeg_filters.log | fzf | awk '{print $2}' | xargs -iabc ffmpeg -h filter=abc
