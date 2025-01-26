import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.items_undertenk_page import ItemPage

def Items_under_10thousand():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.page_load_strategy = 'eager'

        # Path to ChromeDriver
        service = Service('/usr/bin/chromedriver')

        # Setup WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        driver.get("https://www.daraz.com.np")
        
        item_page = ItemPage(driver)
        item_page.search_for_item("Erke fleece jacket")
        item_page.filter_by_price(0, 10000)  # Filter for items under NRs. 10,000

        item_prices = item_page.get_items_prices()

        # Assert that all item prices are less than 10,000
        for price in item_prices:
            assert price < 10000
    finally:
        driver.quit()

if __name__ == "__main__":
    Items_under_10thousand()
