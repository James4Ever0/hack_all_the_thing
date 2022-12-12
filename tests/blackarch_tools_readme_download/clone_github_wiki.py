import parse

# use --depth=1

def gen_git_clone_command(wiki_url):

def check_if_is_repo(url):
    url = url.strip("/")
    format = "https://github.com/{user}/{repo}"
    if parse.parse(format, url):
        wiki_url = url+".wiki.git" # simply wrong