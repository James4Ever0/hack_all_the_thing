import textwrap


def wrapText(textList, width):  # the width is col-1
    content_line_char_count = []
    wrapped_lines = []
    for text in textList:
        lines = textwrap.wrap(text, width=width)
        wrapped_lines.extend(lines)
        lineCount = len(lines)
        content_line_char_count.append(lineCount)
    return wrapped_lines, content_line_char_count


textList = ["123"*20, "1234"] * 2000
wrapText(textList, width=2)