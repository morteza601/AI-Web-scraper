import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


def scrape_website(website):
    print("Lunching the chrome browser ...")

    chrome_driver_path = "I:\AI Webscraper\chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options= options)

    try:
        driver.get(website)
        print("Page Loded ...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

