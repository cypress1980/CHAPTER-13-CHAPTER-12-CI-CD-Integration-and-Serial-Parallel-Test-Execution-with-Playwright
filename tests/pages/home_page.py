"""Home Page Object Model"""
from pages.base_page import BasePage


class HomePage(BasePage):
    """Home Page Object - Manages interactions with the home page after login"""

    EXPECTED_TITLE = "SHOP | QA AUTOMATIONLAB"

    def is_user_logged_in(self):
        """Check if user is logged in by verifying page title"""
        return self.page.title() == self.EXPECTED_TITLE
