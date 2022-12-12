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

import pandas as pd

from read_and_scrape import getURLMap