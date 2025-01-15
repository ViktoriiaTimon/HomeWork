import pytest
from HomeWork.Homework_28.Pages.registration_page import RegistrationPage

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

def test_user_registration(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()

    registration_page.fill_registration_form(
        name="Tom",
        last_name="Smith",
        email="wawov7ne0i@zvvzuv.com",
        password="!123Abc!"
    )
    registration_page.submit_registration()
    check_registration = registration_page.is_registration_successful()
    
    if registration_page.is_registration_successful():
        print("Registration successful")
    else:
        print("User already exists")
    assert check_registration, "User wasnt registered"
