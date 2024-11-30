from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the ChromeDriver executable
driver_path = r"C:\Users\user\Downloads\chromedriver-win64\chromedriver.exe"

# List of user data: username, password, date of birth
user_data = [
    ("ANISHAOZOEMENA1200", "Aziel@123", "1/2/1993"),
    ("MEGANREHM1200", "Aziel@123", "11/20/1994"),
    ("LINDSEYWHEELER1200", "Aziel@123", "9/19/1992"),
    ("JOSHUAREASONOVER1200", "Aziel@123", "1/18/1992"),
    ("JONATHANCLARK1200", "Aziel@123", "2/20/1990"),
    ("JULIANASEWART1200", "Aziel@123", "7/20/1990"),
    ("KRISTIEBEGNAUD1200", "Aziel@123", "9/30/1994"),
]

# Loop through each user
for username, password, dob in user_data:
    # Create a Service object
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://signup.live.com/")

    try:
        # Fill out the email field
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "MemberName"))
        )
        email_field.send_keys(username)
        email_field.send_keys(Keys.RETURN)

        # Wait for the next page to load
        time.sleep(2)

        # Check for CAPTCHA
        try:
            captcha_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "captcha"))
                # Replace with the actual CAPTCHA element ID or class
            )
            print(f"CAPTCHA detected for {username}. Please solve it.")
            input("Press Enter after solving the CAPTCHA...")
        except Exception as e:
            print("No CAPTCHA detected or encountered an issue:", e)

        # Fill out the password field
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Password"))
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Wait for the birthdate page to load
        time.sleep(2)

        # Fill out the date of birth
        birth_date_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "BirthDate"))
        )
        birth_date_field.send_keys(dob)

        # Select country (assumed to be a dropdown, adjust as necessary)
        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Country"))
        )
        country_dropdown.send_keys("United States")  # Adjust if the dropdown requires different input

        # Submit the form
        country_dropdown.send_keys(Keys.RETURN)

        print(f"Account creation process started for {username}.")

    except Exception as e:
        print(f"An error occurred while creating account {username}: {e}")

    finally:
        # Close the driver
        driver.quit()
