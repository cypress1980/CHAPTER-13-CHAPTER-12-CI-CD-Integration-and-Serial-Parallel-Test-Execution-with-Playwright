# Playwright Python Test Automation Framework

A robust test automation framework built with **Playwright** and **Pytest** for cloud-based browser testing on **LambdaTest**.

## 📋 Overview

This framework implements the **Page Object Model (POM)** design pattern for maintainable and scalable test automation. It provides:

- ✅ Cloud-based browser testing via LambdaTest
- ✅ Page Object Model for clean test code
- ✅ Reusable pytest fixtures for test setup
- ✅ Support for multiple browser types
- ✅ Video recording and console logging
- ✅ Cross-platform testing (Windows 10, macOS, Linux)

## 📁 Project Structure

```
CHAPTER_13_PW_PY/
├── tests/
│   ├── config.py                 # LambdaTest configuration & capabilities
│   ├── conftest.py              # Pytest fixtures for browser setup
│   ├── utils.py                 # Utility functions (LambdaTest connection, status)
│   ├── playwright_sample.py     # Test cases
│   └── pages/
│       ├── base_page.py         # Base Page Object with common methods
│       ├── login_page.py        # Login page interactions
│       └── home_page.py         # Home page interactions
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- LambdaTest account (free trial available)

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd CHAPTER_13_PW_PY
   ```

2. **Install dependencies:**
   ```bash
   pip install playwright pytest
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

4. **Set up LambdaTest credentials:**
   ```bash
   export LT_USERNAME="your_lambdatest_username"
   export LT_ACCESS_KEY="your_lambdatest_access_key"
   ```

   Or add to `.env` file and load with:
   ```bash
   source .env
   ```

## 🏗️ Framework Architecture

### Component Layers

```
Tests (playwright_sample.py)
    ↓ (uses fixtures)
Pytest Fixtures (conftest.py)
    ├── browser_setup
    ├── login_page
    └── home_page
    ↓
Page Objects (pages/)
    ├── LoginPage
    ├── HomePage
    └── BasePage
    ↓
Playwright Sync API
    ↓
LambdaTest Cloud Browser
```

### Key Components

#### 1. **config.py** - Configuration
- Defines browser capabilities
- Sets up LambdaTest options (platform, build, recording, etc.)
- Loads credentials from environment variables

#### 2. **conftest.py** - Pytest Fixtures
- `browser_setup`: Initializes browser and page, yields to tests, closes browser
- `login_page`: Creates LoginPage object for login testing
- `home_page`: Creates HomePage object for home page validation

#### 3. **utils.py** - Utility Functions
- `get_lambdatest_browser()`: Connects to LambdaTest cloud
- `set_test_status()`: Reports test results to LambdaTest dashboard

#### 4. **pages/base_page.py** - Base Page Object
Common methods inherited by all page objects:
- `navigate_to(url)` - Navigate to URL
- `fill_text(locator, text)` - Fill input fields
- `click_element(locator)` - Click elements
- `is_element_visible(locator)` - Check element visibility
- `get_text(locator)` - Get element text

#### 5. **pages/login_page.py** - Login Page Object
Encapsulates login page interactions:
- `navigate_to_login()` - Go to login page
- `login(email, password)` - Perform login
- `is_invalid_email_error_visible()` - Check for errors
- Element locators for email, password, button

#### 6. **pages/home_page.py** - Home Page Object
Encapsulates home page interactions:
- `is_user_logged_in()` - Verify successful login by checking page title

## 📝 Writing Tests

### Basic Test Structure

```python
def test_login_success(login_page, home_page, browser_setup):
    """Test successful login"""
    login_page.navigate_to_login()
    login_page.login('demo@demo.com', 'demo')
    assert home_page.is_user_logged_in()
    set_test_status(browser_setup, "passed", "Login successful")
```

### Test Fixtures

Tests automatically receive fixtures:
- `browser_setup`: Playwright page object
- `login_page`: LoginPage object
- `home_page`: HomePage object

### Example Tests

- `test_Login` - Valid credentials login
- `test_Login_Invalid_Email` - Invalid email format
- `test_Login_Wrong_Password` - Wrong password error
- `test_Login_Empty_Email` - Empty email validation
- `test_Login_Empty_Password` - Empty password validation
- `test_Login_Nonexistent_User` - Non-existent user error

## ▶️ Running Tests

### Run all tests
```bash
pytest tests/playwright_sample.py
```

### Run specific test
```bash
pytest tests/playwright_sample.py::test_Login
```

### Run with verbose output
```bash
pytest tests/playwright_sample.py -v
```

### Run with detailed output
```bash
pytest tests/playwright_sample.py -vv
```

### Run with markers (if used)
```bash
pytest tests/ -m "smoke"
```

## 🔧 Configuration

### Browser Capabilities (config.py)

Modify `config.py` to change:
- **Browser**: Chrome, Firefox, Webkit, Edge
- **Version**: Latest or specific version
- **Platform**: Windows 10, macOS, Linux
- **Features**: Video recording, console logs, network logs
- **Geolocation**: For location-based testing
- **Tunnel**: For local app testing

### Example Configuration Change
```python
capabilities = {
    'browserName': 'Firefox',  # Change browser
    'browserVersion': '94',     # Specific version
    'LT:Options': {
        'platform': 'macOS Big Sur',  # Change platform
        'video': True,                # Enable video
        'console': True,              # Capture console
        ...
    }
}
```

## 🌐 Using LambdaTest

### View Test Results
1. Log in to [LambdaTest Dashboard](https://lambdatest.com/)
2. Navigate to **Automation → Builds**
3. View test execution details, videos, and logs

### Benefits
- Run tests on 2000+ real browsers instantly
- Parallel test execution
- Video recording and screenshots
- Network throttling simulation
- Geolocation testing

## 📊 Test Status Reporting

Tests automatically report results to LambdaTest dashboard using:
```python
set_test_status(page, status, remark)
```

**Parameters:**
- `page`: Browser page object
- `status`: "passed" or "failed"
- `remark`: Description of test result

## 🛠️ Troubleshooting

### Browser Connection Issues
- Verify LambdaTest credentials are set
- Check internet connectivity
- Ensure Playwright is installed: `playwright install`

### Test Failures
- Check element locators in page objects
- Verify application URL is accessible
- Review LambdaTest video recordings for visual debugging

### Playwright Errors
```bash
# Reinstall Playwright and browsers
pip install --upgrade playwright
playwright install
```

## 📚 Best Practices

1. **Use Page Objects**: Avoid direct selectors in tests
2. **Meaningful Test Names**: Use descriptive names like `test_login_with_invalid_email`
3. **Assertions in Tests**: Keep assertions in test functions, not page objects
4. **Reusable Methods**: Create methods in BasePage for common actions
5. **Explicit Waits**: Use Playwright's built-in waiting mechanisms
6. **Error Handling**: Check for errors before proceeding
7. **Clean Fixtures**: Ensure proper setup and teardown

## 📖 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [LambdaTest Capabilities Generator](https://www.lambdatest.com/capabilities-generator/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

## 👨‍💻 Contributing

1. Follow the Page Object Model pattern
2. Add tests in `playwright_sample.py`
3. Create page objects in `pages/` directory
4. Update this README with new features

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Support

For issues or questions:
- Check LambdaTest support: [LambdaTest Support](https://www.lambdatest.com/support/)
- Review Playwright docs: [Playwright Python](https://playwright.dev/python/)
- Check pytest plugins: [pytest-playwright](https://github.com/microsoft/playwright-pytest)

---

**Last Updated:** January 2026  
**Framework Version:** Playwright Python with Pytest
