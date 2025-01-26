from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddtoCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "q")  
        self.search_button = (By.CLASS_NAME, 'search-box__button--1oH7')  
        self.price_filter_min = (By.CSS_SELECTOR, 'input[placeholder="Min"]')  
        self.price_filter_max = (By.CSS_SELECTOR, 'input[placeholder="Max"]') 
        self.apply_filter_button = (By.CSS_SELECTOR, 'button[type="button"].ant-btn.yUcnk')  
        self.items = (By.CLASS_NAME, "qmXQo")  
        self.price_tag = (By.CLASS_NAME, "aBrP0")  
        self.item = (By.CLASS_NAME,"qmXQo")
        self.add_cart = (By.XPATH, "//div[@class='pdp-cart-concern']//button[contains(@class, 'add-to-cart-buy-now-btn') and .//span[text()='Add to Cart']]")
        
    def addition_to_cart(self):
        self.driver.find_element(*self.item).click()
        self.driver.find_element(*self.add_cart).click()