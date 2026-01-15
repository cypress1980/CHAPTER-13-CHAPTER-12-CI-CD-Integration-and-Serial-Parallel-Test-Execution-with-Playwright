import json
import urllib
import subprocess
from config import get_capabilities


def get_lambdatest_browser(playwright, browser_name='Chrome'):
    """
    Connect to LambdaTest and return browser instance
    
    Args:
        playwright: Playwright instance
        browser_name: Browser type - 'Chrome', 'Safari', 'Firefox', 'Edge'
    
    Returns:
        Browser instance connected to LambdaTest
    """
    capabilities = get_capabilities(browser_name)
    playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

    lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
        json.dumps(capabilities))
    
    # Connect using the correct browser type engine based on browser
    if browser_name == 'Safari':
        # Safari on LambdaTest requires webkit connection
        browser = playwright.webkit.connect(lt_cdp_url)
    elif browser_name == 'Firefox':
        # Firefox requires firefox connection
        browser = playwright.firefox.connect(lt_cdp_url)
    else:
        # Chrome and Edge use chromium connection
        browser = playwright.chromium.connect(lt_cdp_url)
    
    return browser


def set_test_status(page, status, remark):
    """
    Set test status in LambdaTest dashboard
    """
    page.evaluate("_ => {}",
                  "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")
