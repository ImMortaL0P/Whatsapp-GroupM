import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIG
EXCEL_FILE = "contacts.xlsx"
GROUP_NAME = "MyGroupName"  # Replace with your actual group name
CHROME_DRIVER_PATH = "chromedriver"  # Or give full path if needed

# Load numbers
df = pd.read_excel(EXCEL_FILE)
numbers = df['Phone'].dropna().astype(str).tolist()

# Setup Chrome WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
driver.get("https://web.whatsapp.com/")

# ✅ Wait until search box appears (login complete)
try:
    print("Waiting for QR code scan...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    print("Logged in successfully!")
except TimeoutException:
    print("Login timed out. Please try again.")
    driver.quit()
    exit()

# 🔍 Step 1: Open the group
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
time.sleep(1)
search_box.clear()
search_box.send_keys(GROUP_NAME)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# ℹ️ Step 2: Open group info
driver.find_element(By.XPATH, '//header//div[contains(@title, "Group info")]').click()
time.sleep(2)

# ➕ Step 3: Click "Add participant"
add_participant_xpath = '//div[text()="Add participant"]'
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, add_participant_xpath)))
driver.find_element(By.XPATH, add_participant_xpath).click()
time.sleep(2)

# ➕ Step 4: Add each number
for number in numbers:
    print(f"Trying to add: {number}")
    try:
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        input_box.clear()
        input_box.send_keys(number)
        time.sleep(2)

        # If user appears in search results
        try:
            user_element = driver.find_element(By.XPATH, f'//span[@title="{number}"]')
            user_element.click()
            print(f"Added: {number}")
        except NoSuchElementException:
            print(f"User {number} not found or cannot be added.")
            continue
    except Exception as e:
        print(f"Error with {number}: {e}")
        continue

# ✅ Step 5: Confirm addition
try:
    confirm_button = driver.find_element(By.XPATH, '//span[@data-icon="checkmark"]')
    confirm_button.click()
    print("All users added to group.")
except:
    print("Confirmation failed or no new participants added.")

# Finish
time.sleep(10)
driver.quit()
