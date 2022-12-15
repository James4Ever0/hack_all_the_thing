import subprocess

output = subprocess.check_output(["apt","list"])
#breakpoint()
# skip first "Listing..." line.
from io import StringIO 
formatstr = "{packageName}/{OSName} {versionNum} {platform}"
mio = StringIO(output.decode("utf-8"))
mio.readline()# discard first line
for line in mio.readlines():
#    print("LINE?",line)
    mline = line.strip()
    parsed = parse.parse(formatstr,mline)
    print(parsed)
