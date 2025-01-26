from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.items_above_4_rating_page import ItemsPage
from Pages.items_undertenk_page import ItemPage
def items_with_rating_above_4():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.page_load_strategy = 'eager'

        # Path to ChromeDriver
        service = Service('/usr/bin/chromedriver')

        # Setup WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.daraz.com.np")
        items_page = ItemsPage(driver)
        item_page = ItemPage(driver)
        item_page.search_for_item("Erke fleece jacket")
        item_page.filter_by_price(0,10000)
        items_page.filter_by_rating()
        print("FIltered with rating 4 and above")

    finally:
        driver.quit()

if __name__ == "__main__":
    items_with_rating_above_4()
