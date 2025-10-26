<<<<<<< HEAD
# Facebook Automation Framework

A comprehensive Selenium Behave automation framework for testing Facebook login functionality.

## Project Structure

```
facebook-automation/
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables
├── behave.ini              # Behave configuration
├── README.md               # This file
├── features/               # BDD feature files
│   ├── __init__.py
│   ├── environment.py       # Test environment setup
│   ├── steps/              # Step definitions
│   │   ├── __init__.py
│   │   └── facebook_steps.py
│   └── scenarios/          # Feature files
│       └── facebook_login.feature
├── pages/                  # Page Object Model
│   ├── __init__.py
│   ├── base_page.py        # Base page class
│   └── facebook_login_page.py
├── utils/                  # Utility classes
│   ├── __init__.py
│   ├── driver_manager.py  # WebDriver management
│   └── config.py          # Configuration settings
└── reports/               # Test reports (generated)
```

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   Edit the `.env` file with your Facebook credentials:
   ```env
   FACEBOOK_EMAIL=your_email@example.com
   FACEBOOK_PASSWORD=your_password
   ```

3. **Run the tests:**
   ```bash
   # Run all tests
   behave
   
   # Run specific feature
   behave features/scenarios/facebook_login.feature
   
   # Run in headless mode
   HEADLESS=true behave
   
   # Run with Firefox
   BROWSER=firefox behave
   ```

## Features

- **Page Object Model**: Clean separation of page elements and actions
- **BDD Approach**: Behavior-driven development with Gherkin syntax
- **Multi-browser Support**: Chrome and Firefox
- **Environment Configuration**: Secure credential management
- **Robust Error Handling**: Explicit waits and exception handling
- **Comprehensive Scenarios**: Login, navigation, error handling

## Test Scenarios

1. **Verify Facebook login page elements**
2. **Navigate to forgot password page**
3. **Navigate to sign up page**
4. **Attempt login with invalid credentials**
5. **Login with valid credentials**

## Configuration Options

- `BROWSER`: Browser to use (chrome/firefox)
- `HEADLESS`: Run in headless mode (true/false)
- `IMPLICIT_WAIT`: Implicit wait time in seconds
- `PAGE_LOAD_TIMEOUT`: Page load timeout in seconds
- `FACEBOOK_URL`: Facebook login URL
- `FACEBOOK_EMAIL`: Your Facebook email
- `FACEBOOK_PASSWORD`: Your Facebook password

## Requirements

- Python 3.7+
- Chrome or Firefox browser
- Internet connection
=======
cd# qaengineer-demo
This is my first repository
<br>
Author-Anshu Sharma (Tester 7year experienced)
>>>>>>> 5f51bff8addaeb5b85aaaca8150316efce1fa930
