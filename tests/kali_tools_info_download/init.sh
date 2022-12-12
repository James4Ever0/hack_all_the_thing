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

# get all package names:
# apt list
# you can retrieve package information in apt command, like:
# apt show <package_name>
# you will get homepage link and package description
# if you want package dependencies you will also have it.

# maybe you want to retrieve package information with pacman.
# list all package information just like apt, description, dependencies, homepage and more.
# pacman -Si
# use some parser?
# for aur repos, use yay or yaourt.
# yaourt -Si
# you may use dependencies to deduce relationship between packages, use description, man pages, wiki, manual and tutorials to understand the usage of packages.

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
# hierachical manpages of ubuntu:
# https://manpages.ubuntu.com/manpages
# dman for ubuntu man pages:
# https://manpages.ubuntu.com/dman

# location of locally installed man pages:
# /usr/share/man

# alpine linux is able to download man page alone without installing package: https://georgegarside.com/blog/technology/alpine-linux-install-all-man-pages/
# apk list -I | sed -rn '/-doc/! s/([a-z-]+[a-z]).*/\1/p' | awk '{ print system("apk info \""$1"-doc\" > /dev/null") == 0 ? $ "-doc" : "" }' | xargs apk add

# you may miss the wiki, forum, tutorials. you know where to get them.

# for ruby, you must get all 