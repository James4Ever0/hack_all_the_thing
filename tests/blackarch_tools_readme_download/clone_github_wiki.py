from lib2to3.pytree import type_repr
import parse
import os
os.mkdir("github_wiki")
os.chdir("github_wiki")
# use --depth=1

def gen_git_clone_command(wiki_url):
    return "git clone --depth=1 {}".format(wiki_url)

def check_if_is_repo(url):
    url = url.strip("/")
    format = "https://github.com/{user}/{repo}"
    if parse.parse(format, url):
        wiki_url = url+".wiki.git" # simply wrong


from read_and_scrape import getURLMap

urlmap = getURLMap("tools.csv")
for url, _ in urlmap.items():
    if type(url) == str:
        