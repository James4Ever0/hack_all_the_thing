import parse
fstring = """Package: {}
Version: {}
Priority: {}
Section: {}
Source: {}
Maintainer: {}
Installed-Size: {}
Provides: {}
Pre-Depends: {}
Depends: {}
Suggests: {}
Replaces: {}
Homepage: {homepage}
Tag: {}
Download-Size: {}
APT-Sources: {}
Description: {}
"""

# this fstring is deprecated.
def entryCounter(mstring):
    mfstring = []
    for line in mstring.split("\n"):
        entries = line.split(" ")
        if len(entries)>=1:
            ment = entries[0]
            if ment.endswith(":") and ment.strip() == ment:
                mfstring.append(ment+" {"+ment.replace(":","").replace("-","_")+"}") 
    mres = "\n".join(mfstring)
    #print("MRES?",mres)
    return mres
def parse_apt_info(packageName):
    cmd = ["apt","show",packageName]
    import subprocess
    output = subprocess.check_output(cmd)
    so = output.decode('utf-8')
    #print(so)
    mfstring = entryCounter(so)
    res = parse.parse(mfstring, so)
    print(res)

if __name__ == "__main__":
    pname = "python3"
    parse_apt_info(pname)
