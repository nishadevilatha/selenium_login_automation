from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)  # Keeps Chrome open
options.headless = False  # Makes sure it's visible

# ✅ Replace this path with where you pasted chromedriver.exe
service = Service("C:\\Users\\LENOVO\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
