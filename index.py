from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# Set the paths using Heroku environment variables
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Your web scraping code here
driver.get("https://www.sportybet.com/ng/m/")
print(driver.page_source)
driver.quit()
print("Finished!")
