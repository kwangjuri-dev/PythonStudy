from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set the URL of the webpage to scrape
url = "https://kogpts.vercel.app/"

# Set up Chrome WebDriver (make sure you have Chrome and Chrome WebDriver installed)
chrome_options = Options()
chrome_options.headless = True  # Run in headless mode (no GUI)
service = ChromeService(executable_path='/path/to/chromedriver')  # Replace with the path to your Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the webpage
driver.get(url)

# Wait for the page to load (you can adjust the waiting time as needed)
time.sleep(5)

# Find all div elements with class "rounded-lg border bg-card text-card-foreground shadow-sm Root flex flex-col justify-between"
div_elements = driver.find_elements(By.CSS_SELECTOR, 'div.rounded-lg.border.bg-card.text-card-foreground.shadow-sm.Root.flex.flex-col.justify-between')

# Iterate through the div elements and extract the desired data
for div in div_elements:
    # Find the h3 tag with class "text-lg font-semibold leading-none tracking-tight"
    h3_tag = div.find_element(By.CSS_SELECTOR, 'h3.text-lg.font-semibold.leading-none.tracking-tight')
    h3_text = h3_tag.text.strip()

    # Find the p tag with class "text-sm text-muted-foreground line-clamp-4"
    p_tag = div.find_element(By.CSS_SELECTOR, 'p.text-sm.text-muted-foreground.line-clamp-4')
    p_text = p_tag.text.strip()

    # Find the href value (link address) of the a tag
    a_tag = div.find_element(By.TAG_NAME, 'a')
    href_value = a_tag.get_attribute('href')

    # Print the extracted data
    print("Title:", h3_text)
    print("Description:", p_text)
    print("Link:", href_value)
    print("-----------------------")

# Close the browser
driver.quit()