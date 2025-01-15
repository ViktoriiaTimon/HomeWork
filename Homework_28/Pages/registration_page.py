from selenium.webdriver.common.by import By
from HomeWork.Homework_28.Pages.start_page import StartPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class RegistrationPage(StartPage):
    BUTTON_SIGNUP = (By.XPATH, "//button[@class='hero-descriptor_btn btn btn-primary']")
    INPUT_NAME = (By.XPATH, "//*[@id='signupName']")
    INPUT_LAST_NAME = (By.XPATH, "//*[@id='signupLastName']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='signupEmail']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='signupPassword']")
    INPUT_REPEAT_PASSWORD = (By.XPATH, "//*[@id='signupRepeatPassword']")
    BUTTON_REGISTER = (By.XPATH, "//button[@class='btn btn-primary']")
    USER_NAV_DROPDOWN = (By.ID, "userNavDropdown")

    def open_registration_form(self):
        self.click(self.BUTTON_SIGNUP)

    def fill_registration_form(self, name, last_name, email, password):
        self.enter_text(self.INPUT_NAME, name)
        self.enter_text(self.INPUT_LAST_NAME, last_name)
        self.enter_text(self.INPUT_EMAIL, email)
        self.enter_text(self.INPUT_PASSWORD, password)
        self.enter_text(self.INPUT_REPEAT_PASSWORD, password)

    def submit_registration(self):
        self.click(self.BUTTON_REGISTER)

    def is_registration_successful(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.USER_NAV_DROPDOWN))
            return True
        except TimeoutException:
            return False
