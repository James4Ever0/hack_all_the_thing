# let's ask openai.
# openai you are the best.
# import os
from playwright.sync_api import sync_playwright

# shit! playwright is not running!

# Set the path to the certificate file
# cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?
# targetURL = "https://github.com/dotnetcore/FastGithub"
# timeout = 5000  # 5 seconds? too short?


def getBrowserInstance(p, mProxySettings={"server": "127.0.0.1:38457"}):
    browser = p.chromium.launch(
        proxy=mProxySettings  # seems to be headless. fuck. i ain't see shit. you need to be patient though.
    )  # that shit is faked by openai. it does not read the fucking manual carefully.
    return browser


def browseAndSave(page, targetURL, save_path, timeout=5000):
    page.goto(targetURL)
    # page.wait_for_selector('body') # oh shit does that really work?
    # you should use some timeout strategy.]
    incomplete = True
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
        incomplete = False
    except:
        print(
            "MAYBE TIMEOUT ENCOUNTERED.\nSAVE HTML NO MATTER WHAT.\nTIMEOUT?:", timeout
        )

    # Save the page HTML to a file
    html = page.content()
    with open(save_path, "w+") as f:
        f.write(html)
    return incomplete


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
    from read_and_scrape import getURLMap
    urlmap = getURLMap("tools.csv")
    for targetURL, _ in urlmap.items():
    # targetURL = "https://github.com/dotnetcore/FastGithub"
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".html") as f:
            save_path = f.name
            browseAndSave(page, targetURL, save_path)
    # main loop you should do some thing.

    # Navigate to Google and wait for the page to fully load
    # Close the browser
    browser.close()
