from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ItemsPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_locator = (By.ID, "q")
        self.search_button_locator = (By.CLASS_NAME, 'search-box__button--1oH7')
        self.min_price_locator = (By.CSS_SELECTOR, 'input[placeholder="Min"]')
        self.max_price_locator = (By.CSS_SELECTOR, 'input[placeholder="Max"]')
        self.rating_filter_locator = (By.CSS_SELECTOR, 'button[type="button"].ant-btn.yUcnk')
        self.price_tag = (By.CLASS_NAME, "aBrP0")  
        self.item_rating_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/span')

    def filter_by_rating(self):
        rating_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.item_rating_locator)
        )
        rating_filter.click()
