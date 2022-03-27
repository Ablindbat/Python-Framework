from selenium.webdriver.common.by import By


class SearchPage:

    # locators
    search_textbox_id = "search_query_top"
    search_button_xpath = "//button[@name='submit_search']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Entering search function
    def enter_search_text(self, search_text):
        self.driver.find_element(By.ID, self.search_textbox_id).clear()
        self.driver.find_element(By.ID, self.search_textbox_id).send_keys(search_text)

    #   Clicking search icon
    def click_search_icon(self):
        self.driver.find_element(By.XPATH, "//html").click()
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
