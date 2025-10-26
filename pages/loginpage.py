from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FacebookLoginPage(BasePage):
    # Locators for Facebook login page
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    LOGIN_BUTTON = (By.NAME, "login")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Forgot account?')]")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(), 'Sign up for Facebook')]")
    LOGIN_FORM = (By.ID, "login_form")
    PAGE_TITLE = "Log into Facebook"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self, email):
        """Enter email in the email field"""
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.LOGIN_BUTTON)

    def click_forgot_password(self):
        """Click the forgot password link"""
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def click_create_account(self):
        """Click the create account link"""
        self.click_element(self.CREATE_ACCOUNT_LINK)

    def is_login_form_present(self):
        """Check if login form is present"""
        return self.is_element_present(self.LOGIN_FORM)

    def get_page_title(self):
        """Get the page title"""
        return self.driver.title

    def login(self, email, password):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
