import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

file_path = r'C:\Users\mail2\AppData\Local\Programs\Python\Python312\PYTHON\File upload automation\dist\data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Function to set up and open a new browser window
def setup_browser():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Automatically download and set up ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Open multiple browser windows and navigate to the portal
drivers = []
for index, row in df.iterrows():
    driver = setup_browser()
    driver.get(row['URL'])
    time.sleep(10)  # Wait for the page to load

    file_input = driver.find_element(By.ID, 'uploader_browse')

    try:
        # Locate the file input element (update the selector as needed)
        file_input = driver.find_element(By.ID, 'uploader_browse')
        file_input.click()
        time.sleep(10)
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_path = row['FilePath']
        file_input.send_keys(file_path)
        time.sleep(10)
        # Submit the form or trigger the upload (depends on the specific web page)
        submit_button = driver.find_element(By.ID, 'uploader_start')  # Update selector as needed
        submit_button.click()
        time.sleep(10)  # Wait for the upload to complete
    except Exception as e:
        print(f"Error uploading file {file_path} in window with URL {driver.current_url}: {e}")

# Optional: Close the browser windows after completing the uploads
for driver in drivers:
    driver.quit()
