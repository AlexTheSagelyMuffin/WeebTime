from selenium import webdriver



driver = webdriver.Chrome(executable_path="venv/lib/python3.10/site-packages/chromedriver_binary")
# Navigate to the URL of the form page
driver.get("https://huggingface.co/hakurei/waifu-diffusion")
#get user input on what prompt they want
print("Input Prompt:")
prompt = input()
# Find the form input element and input data into it
input_elem = driver.find_element_by_name("form-input-alt flex-1 rounded-r-none min-w-0 ")
input_elem.send_keys(prompt)
# Submit the form (assuming there is a submit button)
submit_button = driver.find_element_by_css_selector("input[type=submit]")
submit_button.click()
div_element = driver.find_element_by_xpath("/html/body/div/main/div/section[2]/div[3]/div/div/div[4]")
# Check if the div contains an image
if div_element.find_elements_by_tag_name("img"):
    print("The div contains an image")
else:
    print("The div does not contain an image")

# Close the browser window
driver.quit() 