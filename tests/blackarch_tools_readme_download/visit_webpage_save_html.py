# let's ask openai.
# openai you are the best.
# import os
from playwright.sync_api import sync_playwright

# shit! playwright is not running!

# Set the path to the certificate file
# cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?
# targetURL = "https://github.com/dotnetcore/FastGithub"
# timeout = 5000  # 5 seconds? too short?


def getBrowserInstance(
    p,
    # headless=False,
    headless=True,
    mProxySettings={"server": "http://127.0.0.1:38457"},
):
    # not using proxy settings! fuck
    browser = p.chromium.launch(
        headless=headless,
        proxy=mProxySettings,  # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    )  # that shit is faked by openai. it does not read the fucking manual carefully.
    return browser


def browseAndSave(
    page, targetURL, save_path, timeout_0=6500, timeout_1=2500, timeout_2=1000
):  # more countdowns? let's see.
    # page.wait_for_selector('body') # oh shit does that really work?
    # you should use some timeout strategy.]
    incomplete = True
    try:
        page.goto(targetURL, wait_until="domcontentloaded", timeout=timeout_0)
        page.wait_for_load_state("load", timeout=timeout_1)
        incomplete = False
    except:
        print(
            "MAYBE TIMEOUT ENCOUNTERED.\nTRY TO SAVE HTML NO MATTER WHAT.\nTIMEOUTS?:",
            timeout_0,
            timeout_1,
            timeout_2,
        )

    # Save the page HTML to a file
    # html = page.content()
    # playwright._impl._api_types.Error: Unable to retrieve content because the page is navigating and changing the content.
    # wtf?
    # courtesy from openai
    try:
        page.wait_for_selector(
            "html", timeout=timeout_2
        )  # thing will not even show up. no navigation. fuck?
        html = page.content()
        # html = page.evaluate("document.documentElement.outerHTML") # not fucking working?
        # cause you don't have html.
        if type(save_path) == str:
            with open(save_path, "w+") as f:
                f.write(html)
        else:
            save_path.write(html)
            save_path.seek(0)
            # named temporary file?
    except:
        print("HTML not loaded. skipping...")
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
        skip = True # fix NaN issue.
        if type(targetURL) == str:
            if len(targetURL.strip()) > 0:
                skip = False
        if skip:
            continue
        # targetURL = "https://github.com/dotnetcore/FastGithub"
        # save_path = "target.html"
        # fuck tempfile. fuck everything.
        import tempfile

        with tempfile.NamedTemporaryFile("w+", suffix=".html") as f:
            save_path = f.name
            incomplete = browseAndSave(page, targetURL, save_path)
            # now you utilize the function.
            success = False
            # print("FILEPATH?", save_path)
            # print("CONTENT?")
            # cnt = f.read()
            # print(cnt)
            # f.seek(0)
            # it is fucked up.
            try:
                data = read_html(save_path).valueOf()  # will it succeed?
                # fucking shit.
                # print("DATA?",data)
                # breakpoint()
            except:
                data = {}
            data.update({"success": success, "incomplete": incomplete})
            key = targetURL
            upsert_data(key, data)
            # test the tinydb code first. please!
            # many repetitions. but could all be important. what do you want?}
    # main loop you should do some thing.

    # Navigate to Google and wait for the page to fully load
    # Close the browser
    browser.close()
