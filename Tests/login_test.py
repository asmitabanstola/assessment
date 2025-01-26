import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from Pages.login_page import LoginPage
import os

def test_login():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.page_load_strategy = 'eager'

        # Path to ChromeDriver
        service = Service('/usr/bin/chromedriver')

        # Setup WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        #driver.set_page_load_timeout(5)  # Wait up to 30 seconds for a page to load

        # Open website
        driver.get('https://www.daraz.com.np/')
        
        # Create login page object
        login_page = LoginPage(driver)

        #open login page
        login_page.open_login_page()

        # Access the environment variables
        username = os.getenv('DARAZ_USERNAME')
        password = os.getenv('DARAZ_PASSWORD')

        # Perform login
        login_page.enter_username(username)
    
        login_page.enter_password(password)

        login_page.click_login()
        exp="//*[@id='myAccountTrigger' and contains(text(), 'account')]"
        try:
            account_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, exp))
            )
            print("Login Successful")
        except TimeoutException:
            print("Login Failure")

    finally:    
        # Close browser
        driver.quit()

# Run the test
if __name__ == '__main__':
    test_login()