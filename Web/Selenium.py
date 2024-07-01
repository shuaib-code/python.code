from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line to run Chrome in headless mode (no GUI)

# Initialize Chrome driver
chrome_path = "C:\web\chromeDriver/chromedriver.exe"  # Update this path to your ChromeDriver executable
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example URL of the webpage you want to scrape
url = "https://www.wafilife.com/cat/books/author/allama-ibnul-kaiyum-jauyiyah"

# Open the webpage
driver.get(url)

# Wait for the page to load (you might need to adjust the time based on your internet speed)
time.sleep(2)

try:
    # Find all <li> elements under the div with class name 'results-by-facets'
    elements = driver.find_elements(By.CSS_SELECTOR, '.results-by-facets ul li span.woocommerce-Price-amount.amount')

    # Print out the text content of each <li> element found
    for element in elements:
        print(element.text)

finally:
    # Close the browser window
    driver.quit()
