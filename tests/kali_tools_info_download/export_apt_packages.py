import subprocess

output = subprocess.check_output(["apt","list"])
#breakpoint()
import parse
# skip first "Listing..." line.
from io import StringIO 
formatstr = "{packageName}/{OSName} {versionNum} {platform}"
mio = StringIO(output.decode("utf-8"))
mio.readline()# discard first line


packageNames = set()
for line in mio.readlines():
#    print("LINE?",line)
    mline = line.strip()
    parsed = parse.parse(formatstr,mline)
    #print(parsed)
    # we want unique package names.
    packageNames.add(parsed["packageName"])
    try:
        assert parsed is not None
    except:
        print("ERROR PARSING:",mline)
        breakpoint()

print("unique package names:",len(packageNames))

# try to parse info
