import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Load CSV
csv_file = "AIwebsites.csv"
ai_tools_data = pd.read_csv(csv_file)

# Set up Selenium WebDriver
options = Options()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

# Provide the path to ChromeDriver
service = Service("C:\\Users\\amits\\AppData\\Local\\Google\\Chrome for Testing\\chromedriver.exe")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service, options=options)

# Directory to save images
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Iterate through each URL to capture screenshots
for index, row in ai_tools_data.iterrows():
    product_name = row['Product'].replace(" ", "_")  # Sanitize product name for file system
    url = row['URL']
    image_path = os.path.join(images_dir, f"{product_name}.png")

    try:
        driver.get(url)
        driver.save_screenshot(image_path)
        print(f"Screenshot saved for: {product_name}")
    except Exception as e:
        print(f"Failed to capture screenshot for {product_name}: {e}")

# Quit the WebDriver
driver.quit()
print("Screenshots saved in the 'images' folder.")
