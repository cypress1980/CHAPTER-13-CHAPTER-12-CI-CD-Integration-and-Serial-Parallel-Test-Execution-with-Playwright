"""Base Page Object - Contains common methods for all page objects"""


class BasePage:
    """Base class for all page objects"""

    def __init__(self, page):
        """Initialize base page with playwright page object"""
        self.page = page

    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def get_page_title(self):
        """Get the title of the current page"""
        return self.page.title()

    def is_element_visible(self, locator):
        """Check if an element is visible"""
        return self.page.locator(locator).is_visible()

    def is_element_enabled(self, locator):
        """Check if an element is enabled"""
        return self.page.locator(locator).is_enabled()

    def fill_text(self, locator, text):
        """Fill text in an input field"""
        self.page.fill(locator, text)

    def click_element(self, locator):
        """Click on an element"""
        self.page.locator(locator).click()

    def get_text(self, locator):
        """Get text content of an element"""
        return self.page.locator(locator).text_content()

    def close(self):
        """Close the page/browser"""
        self.page.context.browser.close()
