import time
import pytest
from PageObject.LoginPage import LoginPage
from utility.ExcelDataReader import Excel
from selenium.webdriver.common.by import By


@pytest.mark.sanity
class Test_LoginTest:

    @pytest.mark.valid
    def test_loginTest(self, open_browser):
        self.driver = open_browser
        # calling login page from page object
        login = LoginPage(self.driver)
        # Assertion
        title1 = self.driver.title
        assert title1 == "My Store"
        # click
        login.clickSignupLink()
        # assertion
        title2 = self.driver.title
        assert title2 == "Login - My Store"
        # Excel file data retrieving
        excel = Excel()
        data = excel.read_excel("data1")
        # Sending values and actions
        login.enterEmail(data.get("Email"))
        login.enterPassword(data.get("Password"))
        login.clickSignin()
        title = self.driver.title
        # Assertion
        assert title == "My account - My Store"
        # Exit from driver
        self.driver.close()
        self.driver.quit()

    @pytest.mark.invalid
    def test_invalidloginTest(self, open_browser):
        self.driver = open_browser
        # calling login page from page object
        login = LoginPage(self.driver)
        # Assertion
        title1 = self.driver.title
        assert title1 == "My Store"
        login.clickSignupLink()
        # Assertion
        title2 = self.driver.title
        assert title2 == "Login - My Store"
        # Excel file data retrieving
        excel = Excel()
        data = excel.read_excel("data1")
        # Excel file data retrieving
        login.enterEmail(data.get("Email"))
        excel = Excel()
        # Sending values and actions
        datain = excel.read_excel("data2")
        login.enterPassword(datain.get("Password"))
        login.clickSignin()
        # close driver
        self.driver.close()
        self.driver.quit()
