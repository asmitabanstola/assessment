from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "q")  
        self.search_button = (By.CLASS_NAME, 'search-box__button--1oH7')  
        self.price_filter_min = (By.CSS_SELECTOR, 'input[placeholder="Min"]')  
        self.price_filter_max = (By.CSS_SELECTOR, 'input[placeholder="Max"]') 
        self.apply_filter_button = (By.CSS_SELECTOR, 'button[type="button"].ant-btn.yUcnk')  
        self.items = (By.CLASS_NAME, "qmXQo")  
        self.price_tag = (By.CLASS_NAME, "aBrP0")  
        
    def search_for_item(self, item_name):
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        search_box.clear()
        search_box.send_keys(item_name)
        self.driver.find_element(*self.search_button).click()

    def filter_by_price(self, min_price, max_price):
        min_price_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.price_filter_min))
        max_price_input = self.driver.find_element(*self.price_filter_max)
        min_price_input.clear()
        min_price_input.send_keys(str(min_price))
        max_price_input.clear()
        max_price_input.send_keys(str(max_price))
        self.driver.find_element(*self.apply_filter_button).click()

    def get_items_prices(self):
        items = self.driver.find_elements(*self.items)
        prices = []
        for item in items:
            try:
                price = item.find_element(*self.price_tag).text
                prices.append(float(price.replace('NRs.', '').replace(',', '').strip()))
            except:
                continue
        return prices
