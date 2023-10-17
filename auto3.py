from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
# Add any additional options if needed
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
# options.add_argument("--headless")

try:
    # Automatically download and install ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to Google Scholar
    driver.get("https://dnstwister.report/")

    # Wait for a few seconds to let the page load completely
    time.sleep(3)

    # Find the search input field using its name attribute and send keys
    search_input = driver.find_element("name", "domains")
    search_input.send_keys("google.com")

    # Simulate pressing the Enter key
    search_input.send_keys(Keys.RETURN)

    # Wait until the 'qs_rs' div element is present on the page
    time.sleep(90)


    td_elements = driver.find_elements("xpath", "//table[@id='main_report']//tbody//tr//td[1]")

# Create a list to store the extracted text
    domain_list = []

# Iterate through the found elements and extract text, then append to the list
    for td_element in td_elements:
        domain_list.append(td_element.text)

    # Print the extracted domain names
    print(domain_list)

    # Perform further actions with the driver...

finally:
    # Close the browser window if the driver is defined
    if driver:
        driver.quit()