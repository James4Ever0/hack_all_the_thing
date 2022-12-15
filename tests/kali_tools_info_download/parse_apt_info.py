import parse
fstring = """Package: python3
Version: 3.10.6-1
Priority: optional
Section: python
Source: python3-defaults
Maintainer: Matthias Klose <doko@debian.org>
Installed-Size: 92.2 kB
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
