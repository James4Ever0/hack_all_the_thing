curl https://en.kali.tools/all/ > kali_tools_all.html # more tags, more categories, the same as blackarch?
curl https://www.kali.org/tools/ > kali_official.html
curl https://en.kali.tools/ > pentest_tools_with_name.html
# there's also kali-meta page, kali package index, containing homepage link.
# kali meta page on web:
# https://www.kali.org/tools/kali-meta/
# kali meta page on package index:
# http://pkg.kali.org/pkg/kali-meta
# kali package index:
# https://pkg.kali.org/

# you can retrieve package information in apt command, like:
# apt show <package_name>
# you will get homepage link and package description
# if you want package dependencies you will also have it.

# maybe you want to retrieve package information with pacman.

# i remember you have scraped tsinghua pypi index, containing many python tools.
# visit https://pypi.tuna.tsinghua.edu.cn/simple/ to get all package names. but the info is clearly on the other page. you retrieve this from pypi. use the below commandline tool?
# pypi [information|description] <package_name>
# documentation url is provided separately from mainpage.
# what is the commandline tool for searching in pypi?
# https://pypi.org/project/pypi-command-line/
# install it.
# run: pypi search <query>
# it also provides "read-the-docs" to search in documentation of a package, detailed info

# you can download man pages before installing package
# use "dman" by bikeshed
# apt-get install bikeshed
# or browse manpages on web, tutorials on linux and languages
# https://linux.die.net
# man pages with different sections (categories):
# https://linux.die.net/man/

# alpine linux is able to download man page alone without installing package:
# apk 