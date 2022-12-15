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
def entryCounter(mstring,debug=False):
    mfstring = []
    for line in mstring.split("\n"):
        entries = line.split(" ")
        if len(entries)>=1:
            ment = entries[0]
            if ment.endswith(":") and ment.strip() == ment:
                mfstring.append(ment+"{"+ment.replace(":","").replace("-","_")+"}") 
    mres = "\n".join(mfstring)
    if debug:
        print("MRES?",mres)
    return mres
def parse_apt_info(packageNames,debug=False,limit=10):
    cmd = ["apt","show",*packageNames]
    import subprocess
    output = subprocess.check_output(cmd)
    so = "\n"+output.decode('utf-8')
    #print(so)
    prefix="Package: "
    so_splited = so.split("\n"+prefix)
    #cannot split like that.
    for elem in so_splited:
        if len(elem.strip())>limit:
            melem = prefix+elem
            mfstring = entryCounter(melem)
            res = parse.parse(mfstring, melem)
            if debug:
                print("____")
                print(res)
            yield res

if __name__ == "__main__":
    pname = "python3"
    for i in parse_apt_info([pname,'apt']):
        print(i)
