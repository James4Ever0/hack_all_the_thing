from load_demo_data import data

# the data is indeed unstructured.
# split the data with newline.
# we need to check the line number.

# shall we really strip out the trailing white space, causing potential unwanted merges?
# preserve at most one white space in the end? or forcing one white space instead?

# first we want line by line presentation. make sure we get the right array!
# CRLF -> LF should be done before this step. it does not affect readability or structure.

# since we do not have the 'keyword' based highlighter, we can only do line-wise highlighting.

# where's the crlf -> lf ?
data = data.replace("\r\n", "\n")
# the original data, shall be used as reference. save it somewhere, like database.

linewise = data.split("\n")  # there won't be "\n" in the line.


def removeDuplicates(line, chars=[" ", "\t"], maxConsecutiveLength=1):
    for char in chars:
        minUnallowedConsecutiveLength = maxConsecutiveLength + 1
        while True:
            if char * minUnallowedConsecutiveLength in line:
                line = line.replace(
                    char * minUnallowedConsecutiveLength, char * maxConsecutiveLength
                )
            else:
                break
    return line


def lstripChars(line, chars=[" ", "\t"]):
    while True:
        flag = False
        for char in chars:
            if line.startswith(char):
                line = line.lstrip(char)
                flag = True
        if not flag:
            break
    return line


def standardLineCleaner(line):
    line = removeDuplicates(line)
    line = lstripChars(line)
    return line


char_per_group = 30
group_per_conv_group = 3
step_group_for_conv = 2  # instead of 1. just to make sure these conv groups overlap.

# rule to add space: if there's "-" ending, remove the "-" then directly concat with another line.
# if not, then make sure there's one space between two lines.
# create char index to line index mapping.

newContent = ""
newContentCharIndexToLineIndexDict = {}

for lineNumber, line in enumerate(linewise):
    line_cleaned = standardLineCleaner(line)
    # print("{}:".format(lineNumber), line_cleaned)
    if line_cleaned.endswith("-"):
        line_cleaned = line_cleaned[:-1]
    elif not line_cleaned.endswith(" "):
        line_cleaned += " "
    newContent+=line
    newContentCharIndexToLineIndexDict.update()

# we decide to join lines with space no matter what. afterwards we use standard cleaner to remove duplicate spaces.
