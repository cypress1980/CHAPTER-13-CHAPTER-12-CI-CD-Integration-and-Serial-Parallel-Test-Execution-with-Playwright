from utils import set_test_status


def test_Login(login_page, home_page, browser_setup):
    """Test login with valid credentials"""
    login_page.navigate_to_login()
    login_page.login('demo@demo.com', 'demo')
    set_test_status(browser_setup, "passed" if home_page.is_user_logged_in() else "failed",
                   "Login successful - Title matched" if home_page.is_user_logged_in() else "Login failed")


def test_Login_Invalid_Email(login_page, browser_setup):
    """Negative test: Invalid email format"""
    login_page.navigate_to_login()
    login_page.login('invalidemail@', 'demo')
    set_test_status(browser_setup, "passed" if login_page.is_invalid_email_error_visible() else "failed",
                   "Invalid email error displayed")


def test_Login_Wrong_Password(login_page, browser_setup):
    """Negative test: Wrong password"""
    login_page.navigate_to_login()
    login_page.login('demo@demo.com', 'wrongpassword')
    set_test_status(browser_setup, "passed" if login_page.is_invalid_credentials_error_visible() else "failed",
                   "Invalid credentials error displayed")


def test_Login_Empty_Email(login_page, browser_setup):
    """Negative test: Empty email field"""
    login_page.navigate_to_login()
    login_page.login('', 'demo')
    set_test_status(browser_setup, "passed" if login_page.is_email_required_error_visible() else "failed",
                   "Email required error displayed")


def test_Login_Empty_Password(login_page, browser_setup):
    """Negative test: Empty password field"""
    login_page.navigate_to_login()
    login_page.login('demo@demo.com', '')
    set_test_status(browser_setup, "passed" if login_page.is_password_required_error_visible() else "failed",
                   "Password required error displayed")


def test_Login_Nonexistent_User(login_page, browser_setup):
    """Negative test: Non-existent user"""
    login_page.navigate_to_login()
    login_page.login('nonexistent@demo.com', 'demo')
    set_test_status(browser_setup, "passed" if login_page.is_invalid_credentials_error_visible() else "failed",
                   "Invalid credentials error displayed")