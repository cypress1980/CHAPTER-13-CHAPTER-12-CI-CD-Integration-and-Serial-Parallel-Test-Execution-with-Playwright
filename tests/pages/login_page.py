"""Login Page Object Model"""
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login Page Object - Manages all interactions with the login page"""

    # Locators
    EMAIL_INPUT = 'input[id="email"]'
    PASSWORD_INPUT = 'input[id="password"]'
    LOGIN_BUTTON = 'button[id="loginBtn"]'
    INVALID_EMAIL_ERROR = 'text=Please enter a valid email address.'
    INVALID_CREDENTIALS_ERROR = 'text=Invalid email or password!'
    EMAIL_REQUIRED_ERROR = 'text=Please enter your email.'
    PASSWORD_REQUIRED_ERROR = 'text=Please enter your password.'
    LOGIN_URL = "https://shop.qaautomationlabs.com/index.php"

    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate_to(self.LOGIN_URL)

    def enter_email(self, email):
        """Enter email in the email field"""
        self.fill_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.fill_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.LOGIN_BUTTON)

    def is_login_button_visible(self):
        """Check if login button is visible"""
        return self.is_element_visible(self.LOGIN_BUTTON)

    def is_login_button_enabled(self):
        """Check if login button is enabled"""
        return self.is_element_enabled(self.LOGIN_BUTTON)

    def is_error_visible(self, error_type):
        """Check if specific error is visible"""
        error_map = {
            'invalid_email': self.INVALID_EMAIL_ERROR,
            'invalid_credentials': self.INVALID_CREDENTIALS_ERROR,
            'email_required': self.EMAIL_REQUIRED_ERROR,
            'password_required': self.PASSWORD_REQUIRED_ERROR
        }
        return self.is_element_visible(error_map.get(error_type))

    def is_invalid_email_error_visible(self):
        """Check if invalid email error is visible"""
        return self.is_error_visible('invalid_email')

    def is_invalid_credentials_error_visible(self):
        """Check if invalid credentials error is visible"""
        return self.is_error_visible('invalid_credentials')

    def is_email_required_error_visible(self):
        """Check if email required error is visible"""
        return self.is_error_visible('email_required')

    def is_password_required_error_visible(self):
        """Check if password required error is visible"""
        return self.is_error_visible('password_required')

    def login(self, email, password):
        """Perform login with email and password"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
