import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Get user input on what prompt they want
print("Input Prompt:")
prompt = input()

# Set up Selenium WebDriver
driver = webdriver.Chrome("venv/lib/python3.10/site-packages/chromedriver_binary")  # Replace with the path to your chromedriver executable

# Navigate to the URL of the form page
driver.get("https://huggingface.co/hakurei/waifu-diffusion")

# Find the form input element and input data into it
input_elem = driver.find_element(By.XPATH, '/html/body/div/main/div/section[2]/div[3]/div/div/form/div/input')
input_elem.send_keys(prompt)

# Submit the form (assuming there is a submit button)
submit_button = driver.find_element(By.XPATH, "/html/body/div/main/div/section[2]/div[3]/div/div/form/div/button")
submit_button.click()

# Wait for the image to load
time.sleep(5)

# Find the div element containing the image
div_element = driver.find_element(By.XPATH, "/html/body/div/main/div/section[2]/div[3]/div/div/div[4]")

# Check if the div contains an image
while len(div_element.find_elements(By.XPATH, ".//img")) < 1:
    print(div_element.find_elements)
    time.sleep(5)
    div_element = driver.find_element(By.XPATH, "/html/body/div/main/div/section[2]/div[3]/div/div/div[4]")

# Find the image element
image = div_element.find_element(By.XPATH, ".//img")

# Get the image source URL
image_src = image.get_attribute('src')

new_image_src = image_src[5:]
print(new_image_src)

# Specify the path to save the downloaded image
image_path = "C:\\Users\\23achumakov\\Downloads"  # Replace with the desired path and filename to save the image

# Use urllib to download the image
requests.get(new_image_src, image_path)

# Close the browser window
driver.quit()
