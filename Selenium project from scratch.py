from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")


print(driver.title)
driver.quit()