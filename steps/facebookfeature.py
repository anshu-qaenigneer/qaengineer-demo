from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.facebook_login_page import FacebookLoginPage
import os
from dotenv import load_dotenv

load_dotenv()


@given('I am on the Facebook login page')
def step_facebook_login_page(context):
    """Navigate to Facebook login page"""
    context.driver.get(context.facebook_url)
    context.facebook_page = FacebookLoginPage(context.driver)


@when('I enter my email "{email}"')
def step_enter_email(context, email):
    """Enter email in Facebook login form"""
    context.facebook_page.enter_email(email)


@when('I enter my password "{password}"')
def step_enter_password(context, password):
    """Enter password in Facebook login form"""
    context.facebook_page.enter_password(password)


@when('I click the login button')
def step_click_login(context):
    """Click the Facebook login button"""
    context.facebook_page.click_login_button()


@when('I login with credentials from environment')
def step_login_with_env_credentials(context):
    """Login using credentials from environment variables"""
    email = os.getenv('FACEBOOK_EMAIL')
    password = os.getenv('FACEBOOK_PASSWORD')
    context.facebook_page.login(email, password)


@when('I click on "Forgot account?" link')
def step_click_forgot_account(context):
    """Click on forgot account link"""
    context.facebook_page.click_forgot_password()


@when('I click on "Sign up for Facebook" link')
def step_click_sign_up(context):
    """Click on sign up link"""
    context.facebook_page.click_create_account()


@then('I should see the Facebook login form')
def step_see_login_form(context):
    """Verify Facebook login form is present"""
    assert context.facebook_page.is_login_form_present(), "Facebook login form not found"


@then('I should see the email field')
def step_see_email_field(context):
    """Verify email field is present"""
    email_field = context.facebook_page.find_element(context.facebook_page.EMAIL_INPUT)
    assert email_field.is_displayed(), "Email field not visible"


@then('I should see the password field')
def step_see_password_field(context):
    """Verify password field is present"""
    password_field = context.facebook_page.find_element(context.facebook_page.PASSWORD_INPUT)
    assert password_field.is_displayed(), "Password field not visible"


@then('I should see the login button')
def step_see_login_button(context):
    """Verify login button is present"""
    login_button = context.facebook_page.find_element(context.facebook_page.LOGIN_BUTTON)
    assert login_button.is_displayed(), "Login button not visible"


@then('the page title should contain "Log into Facebook"')
def step_page_title_facebook(context):
    """Verify page title contains Facebook login text"""
    title = context.facebook_page.get_page_title()
    assert "Log into Facebook" in title, f"Expected 'Log into Facebook' in title, but got '{title}'"


@then('I should be redirected to Facebook home page')
def step_redirected_to_home(context):
    """Verify redirection to Facebook home page after login"""
    # Wait for navigation and check URL
    WebDriverWait(context.driver, 10).until(
        lambda driver: "facebook.com" in driver.current_url and "login" not in driver.current_url
    )
    current_url = context.driver.current_url
    assert "facebook.com" in current_url, f"Not redirected to Facebook home page. Current URL: {current_url}"


@then('I should see an error message')
def step_see_error_message(context):
    """Verify error message is displayed"""
    # Facebook shows various error messages, check for common ones
    error_selectors = [
        "//div[contains(@class, 'error')]",
        "//div[contains(text(), 'incorrect')]",
        "//div[contains(text(), 'wrong')]",
        "//div[contains(text(), 'invalid')]"
    ]

    error_found = False
    for selector in error_selectors:
        try:
            error_element = context.driver.find_element(By.XPATH, selector)
            if error_element.is_displayed():
                error_found = True
                break
        except:
            continue

    assert error_found, "No error message found"
