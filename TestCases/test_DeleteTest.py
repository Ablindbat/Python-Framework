import time

import pytest

from utility.ExcelDataReader import Excel
from PageObject.DeletePage import DeleteAddressPage


@pytest.mark.sanity
@pytest.mark.delete
@pytest.mark.order(3)
class Test_DeleteTest:

    def test_deleteTest(self, open_browser):
        self.driver = open_browser
        delete = DeleteAddressPage(self.driver)
        # Assertion
        title1 = self.driver.title
        assert title1 == "My Store"

        delete.clickSignupLink()
        # assertion
        title2 = self.driver.title
        assert title2 == "Login - My Store"
        # Excel file data retrieving
        excel = Excel()
        data = excel.read_excel("data3")
        # Sending values and actions
        delete.enterEmail(data.get("Email"))
        delete.enterPassword(data.get("Password"))
        time.sleep(1)
        delete.clickSignin()
        # Assertion
        title4 = self.driver.title
        assert title4 == "My account - My Store"
        delete.click_my_address()
        # Assertion
        title3 = self.driver.title
        assert title3 == "Addresses - My Store"
        delete.click_delete_button()
        delete.popup_action()
        time.sleep(2)
        # close driver
        self.driver.close()
        self.driver.quit()

