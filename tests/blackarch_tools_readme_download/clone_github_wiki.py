import parse

def check_if_is_repo(url):
    format = "https://github.com/{user}/{repo}"
    if parse.parse(format, url):
        wiki_url = url+