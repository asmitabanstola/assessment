from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.search_page import SearchPage

def test_search_erke_fleece_jacket():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    # Path to ChromeDriver
    service = Service('/usr/bin/chromedriver')

    # Setup WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        search_page = SearchPage(driver)
        search_page.open()
        search_page.enter_search_term('fleece jacket erke')
        search_page.click_search_button()
        product_titles = search_page.get_product_titles()
        # Count how many titles contain 'Fleece Jacket'
        matching_titles = [title for title in product_titles if 'Fleece Jacket' in title]
        count = len(matching_titles)
        
        if count > 0:
            print(f"Verification successful: {count} product(s) found with 'Fleece Jacket' in the title.")
        else:
            print("No products found with 'Fleece Jacket' in the title.")

    finally:
        driver.quit()


if __name__ == '__main__':
    test_search_erke_fleece_jacket()
