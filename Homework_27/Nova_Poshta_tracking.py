from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://tracking.novaposhta.ua/#/uk")

input_track = driver.find_element(By.XPATH, "//*[@id='en']")
input_track.send_keys("59001295936666")
button_search = driver.find_element(By.XPATH, "//*[@id='np-number-input-desktop-btn-search-en']")
button_search.click()

time.sleep(2)

status_element = driver.find_element(By.XPATH, "//div[@class='header__status-text']")
status_text = status_element.text

assert status_text == 'Відправлення отримано. Грошовий переказ видано одержувачу.'
print(f'Status is: {status_text}')

time.sleep(5)
driver.quit()