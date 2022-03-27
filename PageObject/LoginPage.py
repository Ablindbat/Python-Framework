from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # locator to Login page
    signup_link_xpath = "//a[@title='Log in to your customer account']"
    # login page locators
    login_email_textbox_id = "email"
    login_password_textbox_id = "passwd"
    login_signin_button_id = "//span[normalize-space()='Sign in']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # click sign up link function
    def clickSignupLink(self):
        self.driver.find_element_by_xpath(self.signup_link_xpath).click()

    # Enter email function
    def enterEmail(self, login_email):
        self.driver.find_element(By.ID, self.login_email_textbox_id).send_keys(login_email)

    # Enter password function
    def enterPassword(self, login_password):
        self.driver.find_element(By.ID, self.login_password_textbox_id).send_keys(login_password)

    # Click sign up function
    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.login_signin_button_id).click()
