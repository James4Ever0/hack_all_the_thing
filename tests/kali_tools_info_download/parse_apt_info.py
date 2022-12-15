import parse
fstring = """Package: python3
Version: 3.10.6-1
Priority: optional
Section: python
Source: python3-defaults
Maintainer: Matthias Klose <doko@debian.org>
Installed-Size: 92.2 kB
Provides: python3-profiler
Pre-Depends: python3-minimal (= 3.10.6-1)
Depends: python3.10 (>= 3.10.6-1~), libpython3-stdlib (= 3.10.6-1)
Suggests: python3-doc (>= 3.10.6-1), python3-tk (>= 3.10.6-1~), python3-venv (>= 3.10.6-1)
Replaces: python3-minimal (<< 3.1.2-2)
Homepage: https://www.python.org/
Tag: devel::interpreter, devel::lang:python, devel::library,
 implemented-in::c, implemented-in::python, role::devel-lib,
 role::program, role::shared-lib
Download-Size: 38.2 kB
APT-Sources:s
Description:
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
