from playwright.sync_api import sync_playwright, expect
from utils import get_lambdatest_browser, set_test_status


def test_Login():
    """
    Test login functionality on LambdaTest
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and login
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        
        # Verify and click login button
        login_button = page.locator('button[id="loginBtn"]')
        expect(login_button).to_be_visible()
        expect(login_button).to_be_enabled()
        login_button.click()
        
        # Verify title after login
        title = page.title()
        if title == "SHOP | QA AUTOMATIONLAB":
            set_test_status(page, "passed", "Title matched")
        else:
            set_test_status(page, "failed", "Title did not match")  
        
        browser.close()


def test_Login_Invalid_Email():
    """
    Negative test: Login with invalid email format
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and attempt login with invalid email
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'invalidemail@')
        page.fill('input[id="password"]', 'demo')
        
        # Click login button
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Verify error message is displayed
        error_message = page.locator('text=Please enter a valid email address.')
        if error_message.is_visible():
            set_test_status(page, "passed", "Invalid email error displayed")
        else:
            set_test_status(page, "failed", "Invalid email error not displayed")
        
        browser.close()


def test_Login_Wrong_Password():
    """
    Negative test: Login with wrong password
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and attempt login with wrong password
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'wrongpassword')
        
        # Click login button
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Verify error message is displayed
        error_message = page.locator('text=Invalid email or password!')
        if error_message.is_visible():
            set_test_status(page, "passed", "Invalid credentials error displayed")
        else:
            set_test_status(page, "failed", "Invalid credentials error not displayed")
        
        browser.close()


def test_Login_Empty_Email():
    """
    Negative test: Login with empty email field
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and attempt login with empty email
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', '')
        page.fill('input[id="password"]', 'demo')
        
        # Click login button
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Verify error message is displayed
        error_message = page.locator('text=Please enter your email.')
        if error_message.is_visible():
            set_test_status(page, "passed", "Email required error displayed")
        else:
            set_test_status(page, "failed", "Email required error not displayed")
        
        browser.close()


def test_Login_Empty_Password():
    """
    Negative test: Login with empty password field
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and attempt login with empty password
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', '')
        
        # Click login button
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Verify error message is displayed
        error_message = page.locator('text=Please enter your password.')
        if error_message.is_visible():
            set_test_status(page, "passed", "Password required error displayed")
        else:
            set_test_status(page, "failed", "Password required error not displayed")
        
        browser.close()


def test_Login_Nonexistent_User():
    """
    Negative test: Login with non-existent user email
    """
    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright)
        page = browser.new_page()

        # Navigate and attempt login with non-existent user
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]', 'nonexistent@demo.com')
        page.fill('input[id="password"]', 'demo')
        
        # Click login button
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Verify error message is displayed
        error_message = page.locator('text=Invalid email or password!')
        if error_message.is_visible():
            set_test_status(page, "passed", "User not found error displayed")
        else:
            set_test_status(page, "failed", "User not found error not displayed")
        
        browser.close()