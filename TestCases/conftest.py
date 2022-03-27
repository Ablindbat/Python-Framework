from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

import utility.config as config


@pytest.fixture()
def open_browser():
    browser = config.browser
    driver = None
    # For chrome browser
    if browser.lower() == "chrome":
        chrome_driver_location = "../drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_location)
        driver.implicitly_wait(1)
        driver.maximize_window()

    # For firefox browser
    elif browser.lower() == "firefox":
        firefox_driver_location = "../drivers/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefox_driver_location)
        driver.maximize_window()
    # For edge browser
    elif browser.lower() == "edge":
        edge_driver_location = "../drivers/msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_driver_location)
        driver.maximize_window()
    # For chrome headless browser
    elif browser.lower() == "headless_chrome":
        chrome_driver_location = "../drivers/chromedriver.exe"
        option = Options()
        option.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=chrome_driver_location, options=option)
    # For firefox headless browser
    elif browser.lower() == "headless_firefox":
        firefox_driver_location = "../drivers/geckodriver.exe"
        option = Options()
        option.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=firefox_driver_location, options=option)
    else:
        print("Browser not supported. Please choose one of them[chrome,firefox & edge]")

    # get in base Url
    driver.get(config.baseUrl)
    return driver

