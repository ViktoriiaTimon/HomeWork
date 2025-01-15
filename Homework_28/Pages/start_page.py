from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class StartPage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(ec.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element.text
