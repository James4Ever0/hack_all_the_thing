import textwrap

textList = ["123", "1234"] * 2000


def wrapText(textList, width):  # the width is col-1
    content_line_char_count = []
    wrapped_lines = []
    for text in textList:
        lines = textwrap.wrap(text, width=width)
        wrapped_lines.extend(lines)
        lineCount = len(lines)
        content_line_char_count.append(lineCount)
    return wrapped_lines, content_line_char_count


