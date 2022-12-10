# let's ask openai.
# openai you are the best.
# import os
from playwright.sync_api import sync_playwright

# shit! playwright is not running!

# Set the path to the certificate file
# cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?
# targetURL = "https://github.com/dotnetcore/FastGithub"
# timeout = 5000  # 5 seconds? too short?


def getBrowserInstance(p, headless=False,mProxySettings={"server": "http://127.0.0.1:38457"}):
    # not using proxy settings! fuck
    browser = p.chromium.launch(headless=headless,
        proxy=mProxySettings  # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    )  # that shit is faked by openai. it does not read the fucking manual carefully.
    return browser


def browseAndSave(page, targetURL, save_path, timeout_0=5000,timeout_1 = 2000):
    # page.wait_for_selector('body') # oh shit does that really work?
    # you should use some timeout strategy.]
    incomplete = True
    try:
        page.goto(targetURL,wait_until="domcontentloaded",timeout=timeout_0)
        page.wait_for_load_state("load",timeout=timeout_1)
        incomplete = False
    except:
        print(
            "MAYBE TIMEOUT ENCOUNTERED.\nSAVE HTML NO MATTER WHAT.\nTIMEOUT?:", timeout
        )

    # Save the page HTML to a file
    html = page.content()
    if type(save_path) == str:
        with open(save_path, "w+") as f:
            f.write(html)
    else:
        save_path.write(html)
        save_path.seek(0)
        # named temporary file?
    return incomplete

from read_and_scrape import getURLMap
from readability_use_mozilla_test import read_html
from tinydb_upsert import upsert_data
import progressbar

# Create a Playwright instance and launch browser
with sync_playwright() as p:
    # mProxySettings = {"server": "127.0.0.1:38457"}  # whatever.
    # browser = p.chromium.launch(
    #     proxy=mProxySettings # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    # )  # that shit is faked by openai. it does not read the fucking manual carefully.
    browser = getBrowserInstance(p)
    # Create a new page and set the HTTP proxy
    page = browser.new_page()  # just use the same damn page.
    # does that work?
    urlmap = getURLMap("tools.csv")
    for targetURL, _ in progressbar.progressbar(urlmap.items()):
    # targetURL = "https://github.com/dotnetcore/FastGithub"
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".html") as f:
            save_path = f.name
            incomplete = browseAndSave(page, targetURL, save_path)
            # now you utilize the function.
            success = False
            try:
                data = read_html(save_path) # will it succeed?
            except:
                data = {}
            data.update({'success': success,'incomplete':incomplete})
            key = targetURL
            upsert_data(key,data)
            # test the tinydb code first. please!
            # many repetitions. but could all be important. what do you want?
    # main loop you should do some thing.

    # Navigate to Google and wait for the page to fully load
    # Close the browser
    browser.close()
