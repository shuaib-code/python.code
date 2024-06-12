from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://www.google.com')

search_box = driver.find_element_by_name('q')
search_box.send_keys('Python web automation')
search_box.send_keys(Keys.RETURN)

# Perform further actions or extract information
driver.quit()
# Does not work. Investigate further on later.