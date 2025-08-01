# download_tanks.py
# Copyright (c) 2025 nasro90dz
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# === CONFIGURATION ===
CHROMEDRIVER_PATH = r"C:\Path\To\chromedriver.exe"       # Replace with actual path
DOWNLOAD_DIR = r"C:\Path\To\Download"                    # Replace with desired download folder
DOWNLOAD_URL = "http://example.local/files/"             # Replace with actual URL
TARGET_FILE_NAME = "Tanks.csv"                           # File to download


# === SETUP BROWSER OPTIONS ===
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# === DELETE EXISTING FILE IF EXISTS ===
target_path = os.path.join(DOWNLOAD_DIR, TARGET_FILE_NAME)
if os.path.exists(target_path):
    print(f"[INFO] Removing existing file: {TARGET_FILE_NAME}")
    os.remove(target_path)

# === START SELENIUM DRIVER ===
print("[INFO] Starting Chrome WebDriver...")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    print(f"[INFO] Navigating to: {DOWNLOAD_URL}")
    driver.get(DOWNLOAD_URL)
    time.sleep(3)  # wait for page to load

    print(f"[INFO] Looking for file link: {TARGET_FILE_NAME}")
    file_link = driver.find_element(By.LINK_TEXT, TARGET_FILE_NAME)
    file_link.click()
    print("[INFO] File link clicked. Download should be starting...")

    time.sleep(10)  # wait for download to complete

    if os.path.exists(target_path):
        print(f"[SUCCESS] File downloaded: {target_path}")
    else:
        print("[ERROR] File was not downloaded.")

except Exception as e:
    print(f"[ERROR] An exception occurred:\n{e}")

finally:
    print("[INFO] Closing browser.")
    driver.quit()
