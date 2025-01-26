from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.add_to_cart_page import AddtoCartPage
from Pages.items_undertenk_page import ItemPage

def add_to_cart():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.page_load_strategy = 'eager'

        # Path to ChromeDriver
        service = Service('/usr/bin/chromedriver')

        # Setup WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        driver.get("https://www.daraz.com.np")
        item_page=ItemPage(driver)
        add_cart_page = AddtoCartPage(driver)
        item_page.search_for_item("Erke fleece jacket")
        item_page.filter_by_price(0, 10000)  # Filter for items under NRs. 10,000
        driver.implicitly_wait(20)
        add_cart_page.addition_to_cart()
        print("Add to Cart Successfull")

    finally:
        driver.quit()

if __name__ == "__main__":
    add_to_cart()
