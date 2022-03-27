import time

import pytest

from PageObject.SignUpPage import Signup
from utility.ExcelDataReader import Excel


@pytest.mark.sanity
@pytest.mark.signup
@pytest.mark.order(1)
class Test_SignupTest:

    def test_signup(self, open_browser):
        self.driver = open_browser
        sign = Signup(self.driver)
        # Assertion
        title1 = self.driver.title
        assert title1 == "My Store"
        sign.click_signup_link()
        # assertion
        title2 = self.driver.title
        assert title2 == "Login - My Store"
        # Excel file data retrieving
        excel = Excel()
        data = excel.read_excel("data2")
        # Sending values and actions
        sign.enter_email_address(data.get("Email"))
        print(data.get("Email"))
        sign.click_create_an_account()
        # Assertion
        after_enter_email = self.driver.title
        assert after_enter_email == "Login - My Store"
        time.sleep(5)
        # Sending values and actions
        sign.click_title(data.get("Gender"))
        time.sleep(5)
        sign.enter_personal_information_firstname(data.get("Firstname"))
        sign.enter_personal_information_lastname(data.get("Lastname"))
        sign.enter_password(data.get("Password"))
        sign.select_date_of_birth(str(data.get("Day")), str(data.get("Month")), str(data.get("Year")))
        sign.click_news_letter()
        sign.click_offer_mail()
        sign.enter_address_firstname(data.get("address_firstname"))
        sign.enter_address_lastname(data.get("address_lastname"))
        sign.enter_company_name(data.get("Company"))
        sign.enter_address(data.get("address1"))
        sign.enter_address_line2(data.get("address2"))
        sign.enter_city(data.get("city"))
        sign.select_state(data.get("state"))
        sign.enter_pin_code(data.get("pincode"))
        sign.enter_other_information(data.get("otherinfo"))
        sign.enter_home_phone(data.get("phone"))
        sign.enter_mobile_number(data.get("mobile"))
        sign.enter_address_alias(data.get("addressalias"))
        sign.click_register()
        # Assertion
        title3 = self.driver.title
        assert title3 == "My account - My Store"
        # driver close
        self.driver.close()
        self.driver.quit()
