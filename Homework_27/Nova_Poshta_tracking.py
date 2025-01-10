from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://tracking.novaposhta.ua/#/uk")

wait = WebDriverWait(driver, 5)

input_track = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='en']")))
input_track.send_keys("59001295936666")
button_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='np-number-input-desktop-btn-search-en']")))
button_search.click()


status_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header__status-text']")))
status_text = status_element.text

assert status_text == 'Відправлення отримано. Грошовий переказ видано одержувачу.'
print(f'Status is: "{status_text}"')

driver.quit()
