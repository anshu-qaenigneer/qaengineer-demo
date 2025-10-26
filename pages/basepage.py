from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator}")

    def find_elements(self, locator):
        """Find multiple elements"""
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """Click element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Send keys to element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        """Check if element is present"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False