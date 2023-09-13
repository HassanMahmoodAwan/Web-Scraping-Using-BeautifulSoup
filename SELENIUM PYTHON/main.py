

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.techwithtim.net')

print(driver.title)
search = driver.find_elements("txtKeywords")
time.sleep(5)
#driver.quit()