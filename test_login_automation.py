from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
options.headless = False

service = Service("C:\\Users\\LENOVO\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# ✅ Open demo login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# ✅ Fill username and password
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# ✅ Click the login button
driver.find_element(By.ID, "submit").click()

# Optional wait to see result
time.sleep(5)
# driver.quit()
