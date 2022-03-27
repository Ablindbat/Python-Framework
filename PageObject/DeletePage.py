from selenium.webdriver.common.by import By


class DeleteAddressPage:

    # locator to Login page
    signup_link_xpath = "//a[@title='Log in to your customer account']"

    # login page locators
    login_email_textbox_id = "email"
    login_password_textbox_id = "passwd"
    login_signin_button_id = "//span[normalize-space()='Sign in']"

    # My address xpath
    my_address_button_xpath = "//span[normalize-space()='My addresses']"

    # delete button xpath
    delete_button_xpath = "//span[normalize-space()='Delete']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # clicking signup link function
    def clickSignupLink(self):
        self.driver.find_element_by_xpath(self.signup_link_xpath).click()

    # Entering email function
    def enterEmail(self, login_email):
        self.driver.find_element(By.ID, self.login_email_textbox_id).send_keys(login_email)

    # Entering password function
    def enterPassword(self, login_password):
        self.driver.find_element(By.ID, self.login_password_textbox_id).send_keys(login_password)

    # clicking sign in function
    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.login_signin_button_id).click()

    # clicking my address button function
    def click_my_address(self):
        self.driver.find_element(By.XPATH, self.my_address_button_xpath).click()

    # clicking delete button function
    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.delete_button_xpath).click()

    # Action on pop function
    def popup_action(self):
        alert_element = self.driver.switch_to.alert
        alert_element.accept()
