
import parse
import os
from read_and_scrape import getURLMap

urlmap = getURLMap("tools.csv")

try:
    os.mkdir("github_wiki")
except:
    pass
os.chdir("github_wiki")
# use --depth=1

def gen_git_clone_command(wiki_url):
    return "git clone --depth=1 {}".format(wiki_url)

def check_if_is_repo(url):
    url = url.strip("/")
    format = "https://github.com/{user}/{repo}"
    if parse.parse(format, url):
        wiki_url = url+".wiki.git" # simply wrong
        return wiki_url



import progressbar
for url, _ in progressbar.progressbar(urlmap.items()):
    if type(url) == str:
        wiki_url = check_if_is_repo(url)
        if wiki_url:
            cmd = gen_git_clone_command(wiki_url)
            os.system(cmd)