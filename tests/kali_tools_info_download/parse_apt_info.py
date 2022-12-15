import parse
fstring = """Package: python3
Version: Priority: {}
Section: {}
Source: {}
Maintainer: {}
Installed-Size: {}
Provides: {}
Pre-Depends: {}
Depends: {}
Suggests: {}
Replaces: {}
Homepage: {}
Tag: {}
Download-Size: {}
APT-Sources: {}
Description: {}
"""
def parse_apt_info(packageName):
    cmd = ["apt","show",packageName]
    import subprocess
    output = subprocess.check_output(cmd)
    so = output.decode('utf-8')
    print(so)

if __name__ == "__main__":
    pname = "python3"
    parse_apt_info(pname)
