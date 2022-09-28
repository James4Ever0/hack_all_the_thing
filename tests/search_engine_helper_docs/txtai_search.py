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
data = data.replace("\r\n","\n")
# the original data, shall be used as reference. save it somewhere, like database.

linewise = data.split("\n")


def removeDuplicates(line, chars=[" ","\t"], maxConsecutiveLength=1):

def lstripChars(line, chars=[" ","\t"]):

for lineNumber, line in enumerate(linewise):
    print("{}:".format(lineNumber),line)