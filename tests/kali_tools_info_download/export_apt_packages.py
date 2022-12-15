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
targetCols = ["Homepage","Tag","Description"]

data = {x:[] for x in (["Name"]+targetCols)}
import pandas as pd
import progressbar as pg
for pname in pg.progressbar(packageNames):
    from parse_apt_info import parse_apt_info
    info = parse_apt_info(pname)
    #if info is not None:
        data['Name'].append(pname)
        mdict = info.named
        mdict = {key:val.strip() for key,val in mdict.items()}
        for col in targetCols:
            data[col].append(mdict.get(col,None))
            # the Result class is composed of "fixed" and "named", cannot be directly converted to dictionary
        print({x:info[x] for x in targetCols if x in mdict.keys()})
    else:
        parse_apt_info(pname,debug=True)
        breakpoint()
df = pd.DataFrame(data)
df.to_csv("kali_apt_packages_info.csv",index=False)
