import time

import pytest

from PageObject.SearchPage import SearchPage

import utility.config as config


@pytest.mark.sanity
class Test_Search:

    def test_search(self, open_browser):
        self.driver = open_browser
        # calling search page
        search = SearchPage(self.driver)
        # Retrieving data from config.py file
        search.enter_search_text(config.search_text)
        time.sleep(1)
        search.click_search_icon()
        time.sleep(5)
        # driver close
        self.driver.close()
        self.driver.quit()
