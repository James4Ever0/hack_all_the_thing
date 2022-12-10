# let's ask openai.
# openai you are the best.
# import os
from playwright.sync_api import  sync_playwright

# Set the path to the certificate file
# cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?
targetURL = "https://github.com/dotnetcore/FastGithub"
timeout = 5000 # 5 seconds? too short?

# Create a Playwright instance and launch browser
with sync_playwright() as p:
    mProxySettings = {
              'server': '127.0.0.1:38457'
            } # whatever.
    browser = p.chromium.launch(proxy=mProxySettings) # that shit is faked by openai. it does not read the fucking manual carefully.
    # Create a new page and set the HTTP proxy
    page = browser.new_page()
    # does that work?

    # Navigate to Google and wait for the page to fully load
    page.goto(targetURL)
    # page.wait_for_selector('body') # oh shit does that really work?
    # you should use some timeout strategy.
    try:
        page.wait_for_load_state('networkidle',timeout=timeout)
    except:
        print("MAYBE TIMEOUT ")

    # Save the page HTML to a file
    html = page.content()
    with open('target.html', 'w') as f:
        f.write(html)

    # Close the browser
    browser.close()


