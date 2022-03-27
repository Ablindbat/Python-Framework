import time

import pytest

from PageObject.NewAddressPage import NewAddressPage
from utility.ExcelDataReader import Excel


@pytest.mark.sanity
@pytest.mark.newadsress
@pytest.mark.order(2)
class Test_NewAddress:

    def test_new_address(self, open_browser):
        self.driver = open_browser
        # calling login page from page object
        new_address = NewAddressPage(self.driver)
        # Assertion
        title1 = self.driver.title
        assert title1 == "My Store"
        new_address.clickSignupLink()
        # assertion
        title2 = self.driver.title
        assert title2 == "Login - My Store"
        # Excel file data retrieving
        excel = Excel()
        data = excel.read_excel("data3")
        # Sending values and actions
        new_address.enterEmail(data.get("Email"))
        new_address.enterPassword(data.get("Password"))
        new_address.clickSignin()
        # Assertion
        title3 = self.driver.title
        assert title3 == "My account - My Store"
        new_address.click_my_address()
        # Assertion
        title4 = self.driver.title
        assert title4 == "Addresses - My Store"
        new_address.click_add_new_button()
        # Assertion
        title5 = self.driver.title
        assert title5 == "Address - My Store"
        # Sending values and actions
        new_address.enter_firstname(data.get("Firstname"))
        new_address.enter_lastname(data.get("Lastname"))
        new_address.enter_company_name(data.get("Company"))
        new_address.enter_address(data.get("address1"))
        new_address.enter_address_line2(data.get("address2"))
        new_address.enter_city(data.get("city"))
        new_address.select_state(data.get("state"))
        new_address.enter_postal_code(data.get("pincode"))
        new_address.enter_home_phone(data.get("phone"))
        new_address.enter_mobile_phone(data.get("mobile"))
        new_address.enter_additional_info(data.get("otherinfo"))
        new_address.enter_address_alias(data.get("addressalias"))
        new_address.click_save_button()
        time.sleep(10)
        # closing driver
        self.driver.close()
        self.driver.quit()

