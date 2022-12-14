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

# do it like: [packageNames[i:i+n] for i in range(0, len(packageNames),n)]
# or: iter(lambda: islice(miter,n)),())
from itertools import islice
n = 1000
miter = iter(packageNames)
for pnames in pg.progressbar(iter(lambda: islice(miter,n),())):
    pnames = list(pnames)
    if len(pnames) == 0:
        break
    from parse_apt_info import parse_apt_info
    infos = parse_apt_info(pnames,debug=True)
    for info in infos:
        if info is not None:
            mdict = info.named
            mdict = {key:val.strip() for key,val in mdict.items()}
            pname = mdict.get("Package",None)
            if pname is None:
                continue
            pname = pname.strip()
            data['Name'].append(pname)
            for col in targetCols:
                data[col].append(mdict.get(col,None))
                # the Result class is composed of "fixed" and "named", cannot be directly converted to dictionary
            print({x:info[x] for x in targetCols if x in mdict.keys()})
        else:
            #parse_apt_info(pname,debug=True)
            breakpoint()
df = pd.DataFrame(data)
df.to_csv("kali_apt_packages_info.csv",index=False)
