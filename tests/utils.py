import json
import urllib
import subprocess
from config import capabilities


def get_lambdatest_browser(playwright):
    """
    Connect to LambdaTest and return browser instance
    """
    playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion

    lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
        json.dumps(capabilities))
    browser = playwright.chromium.connect(lt_cdp_url)
    return browser


def set_test_status(page, status, remark):
    """
    Set test status in LambdaTest dashboard
    """
    page.evaluate("_ => {}",
                  "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")
