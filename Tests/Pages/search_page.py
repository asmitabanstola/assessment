from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.daraz.com.np/'
        self.search_box_locator = (By.NAME, 'q')  # Locator for the search input field
        self.search_button_locator = (By.CLASS_NAME, 'search-box__button--1oH7')  # Locator for the search button
        self.product_titles_locator = (By.CLASS_NAME, 'RfADt')  # Locator for product titles in search results

    def open(self):
        self.driver.get(self.base_url)

    def enter_search_term(self, term):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(term)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()

    def get_product_titles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_titles_locator)
        )
        products = self.driver.find_elements(*self.product_titles_locator)
        return [product.text for product in products]
