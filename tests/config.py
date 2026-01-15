import os


def get_capabilities(browser_name='Chrome'):
    """
    Get LambdaTest capabilities for specified browser
    
    Args:
        browser_name: Browser type - 'Chrome', 'Safari', 'Firefox', 'Edge'
    
    Returns:
        dict: Capabilities dictionary for LambdaTest
    """
    base_capabilities = {
        'browserVersion': 'latest',
        'LT:Options': {
            'platform': 'macOS Sequoia' if browser_name == 'Safari' else 'Windows 11',
            'build': 'Playwright Python Build',
            'name': f'Playwright Python Test - {browser_name}',
            'user': os.getenv('LT_USERNAME'),
            'accessKey': os.getenv('LT_ACCESS_KEY'),
            'network': True,
            'video': True,
            'console': True,
            'tunnel': False,
            'tunnelName': '',
            'geoLocation': '',
            'playwrightClientVersion': '1.56.0',
        }
    }
    
    # Browser-specific mappings for LambdaTest
    # Safari on LambdaTest uses 'pw-webkit' browser name
    browser_mappings = {
        'Chrome': 'Chrome',
        'Safari': 'pw-webkit',  # LambdaTest uses pw-webkit for Safari
        'Firefox': 'Firefox',
        'Edge': 'MicrosoftEdge'
    }
    
    base_capabilities['browserName'] = browser_mappings.get(browser_name, 'Chrome')
    
    # Safari requires macOS
    if browser_name == 'Safari':
         capabilities['browserName'] = 'pw-webkit'
         capabilities['LT:Options']['platform'] = 'macOS Sequoia'
    
    return base_capabilities


# Default configuration (Chrome)
capabilities = get_capabilities('Chrome')
