githubimport time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException  # Import StaleElementReferenceException

# Function to wait for an element to be present on the page

def click_all_checkboxes(driver):
    # Find all checkboxes on the page
    checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

    # Click each checkbox
    for checkbox in checkboxes:
        checkbox.click()


# Replace 'form_url' with the actual URL of your form
form_url = ''

# Start a new instance of the Chrome driver
driver = webdriver.Chrome()

# Number of submissions
submissions = 1  # Change this to the desired number of submissions

next_buttons = driver.find_elements(By.XPATH, '//button[text()="Next"]')

for _ in range(submissions):
    driver.get(form_url)

    print("Waiting for start now button...")
    start_now_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-main-content1"]/div/div[3]/div[3]/button/div')))
    print("Start now button found!")

    start_now_button.click()

    # Locate and click the "Next" N number of times
    for _ in range(#Number of times#):
        try:
            # Wait for the "Next" button to be clickable
            next_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            next_button.click()
            print("Next button clicked.")
            time.sleep(2)  # Pause to avoid rate limiting or being blocked
        except Exception as e:
            print(f"Error clicking Next button: {e}")
    click_all_checkboxes(driver)
    # Locate the input field
    input_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Single line text"]')))
    
    # Generate a random full name
    random_full_name = f"RandomName_{random.randint(1, 100)}"
    
    # Enter the random full name into the input field
    input_field.send_keys(random_full_name)
    # Locate the date input field
    date_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="DatePicker0-label"]')))

    # Click on the date input field to open the date picker
    date_input.click()
    # Press Enter to select the date
    date_input.send_keys(Keys.RETURN)
    # Next to the next page
    next_button.click()

def select_random_radio():
    # Select random radio button options
    radio_groups = driver.find_elements(By.XPATH, '//*[@data-automation-id="questionItem"]')
    for radio_group in radio_groups:
        radio_buttons = radio_group.find_elements(By.XPATH, './/input[@type="radio"]')
        if radio_buttons:
            random.choice(radio_buttons).click()
                # Select a random number of checkboxes
    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]'))
    )
    for checkbox in random.sample(checkboxes, k=random.randint(0, len(checkboxes))):
        checkbox.click()

# Main loop to navigate through pages
while True:
    # Perform actions on the current page
    """select_random_checkboxes()"""
    select_random_radio()

    # Look for the "Next" button
    next_buttons = driver.find_elements(By.XPATH, '//button[text()="Next"]')

    # Check if there's at least one "Next" button
    if next_buttons:
        # Click the first "Next" button
        next_buttons[0].click()
    else:
        submit_buttons = driver.find_elements(By.XPATH, '//button[text()="Submit"]')
                # Click the first "Submit" button
        submit_buttons[0].click()
# Close the WebDriver
driver.quit()
