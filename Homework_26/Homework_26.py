from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

driver.switch_to.frame("frame1")

input1 = driver.find_element(By.ID, "input1")
input1.send_keys("Frame1_Secret")
button1 = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
button1.click()

time.sleep(1)
alert1 = Alert(driver)
print(f'Alert: {alert1.text}')
alert1.accept()

driver.switch_to.default_content()

driver.switch_to.frame("frame2")
input2 = driver.find_element(By.ID, "input2")
input2.send_keys("Frame2_Secret")
button2 = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
button2.click()

time.sleep(1)
alert2 = Alert(driver)
print(f'Alert: {alert2.text}')
alert2.accept()

driver.switch_to.default_content()
driver.quit()