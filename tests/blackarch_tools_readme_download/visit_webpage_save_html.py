# let's ask openai.
# openai you are the best.
# import os
from playwright.sync_api import sync_playwright

# shit! playwright is not running!

# Set the path to the certificate file
# cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?
# targetURL = "https://github.com/dotnetcore/FastGithub"
# timeout = 5000  # 5 seconds? too short?

def getBrowserInstance(p,mProxySettings = {"server": "127.0.0.1:38457"} ):
    browser = p.chromium.launch(
        proxy=mProxySettings # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    )  # that shit is faked by openai. it does not read the fucking manual carefully.
    return browser

def browseAndSave(page,targetURL, save_path, timeout = 5000):

# Create a Playwright instance and launch browser
with sync_playwright() as p:
    # mProxySettings = {"server": "127.0.0.1:38457"}  # whatever.
    # browser = p.chromium.launch(
    #     proxy=mProxySettings # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    # )  # that shit is faked by openai. it does not read the fucking manual carefully.
    browser = getBrowserInstance(p)
    # Create a new page and set the HTTP proxy
    page = browser.new_page() # just use the same damn page.
    # does that work?

    # Navigate to Google and wait for the page to fully load
    # Close the browser
    browser.close()
