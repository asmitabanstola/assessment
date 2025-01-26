from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login = (By.ID,"anonLogin")
        self.username_textbox = (By.XPATH, "//input[@placeholder='Please enter your Phone Number or Email']")
        self.password_textbox = (By.XPATH, "//input[@class='iweb-input' and @type='password']")
        self.login_button = (By.XPATH, "//button[text()='LOG IN']")
        self.wait = WebDriverWait(driver, 30)

    def open_login_page(self):
        self.driver.find_element(*self.login).click()
        

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*  self.login_button).click()
    