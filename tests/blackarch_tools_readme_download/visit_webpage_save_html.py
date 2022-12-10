# let's ask openai.
# openai you are the best.
import os
from playwright.sync_api import Playwright, sync_playwright

# Set the path to the certificate file
cert_path = '/opt/fastgithub/cacert/fastgithub.cer' # where is the path of fastgithub?

# Create a Playwright instance and launch browser
with sync_playwright() as p:
# Set browser to use the certificate for HTTPS connections
browser_context_options = {
"https_certificates": [{
"certificate_chain": [open(cert_path, "rb").read()]
}]
}
browser = p.chromium.launch(browser_context_options=browser_context_options)

# Create a new page and set the HTTP proxy
page = browser.new_page()
# does that work?
page.set_http_proxy('http://localhost:38457')
page.set_https_proxy('http://localhost:38457')

# Navigate to Google and wait for the page to fully load
page.goto('https://google.com')
page.wait_for_selector('body')

# Save the page HTML to a file
html = page.content()
with open('google.html', 'w') as f:
    f.write(html)

# Close the browser
browser.close()


