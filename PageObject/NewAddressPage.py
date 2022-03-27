from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class NewAddressPage:
    # locator to Login page
    signup_link_xpath = "//a[@title='Log in to your customer account']"
    # login page locators
    login_email_textbox_id = "email"
    login_password_textbox_id = "passwd"
    login_signin_button_id = "//span[normalize-space()='Sign in']"
    # My address xpath
    my_address_button_xpath = "//span[normalize-space()='My addresses']"
    # Add new address xpath
    add_new_address_button_xpath = "//span[normalize-space()='Add a new address']"

    # locators of address section
    firstname_textbox_id = "firstname"
    lastname_textbox_id = "lastname"
    company_textbox_id = "company"
    address_textbox_id = "address1"
    address_line2_textbox_id = "address2"
    city_textbox_id = "city"
    state_select_id = "id_state"
    pin_code_textbox_id = "postcode"
    home_phone_textbox_id = "phone"
    mobile_textbox_id = "phone_mobile"
    additional_information_textarea_id = "other"
    alias_name_textbox_id = "alias"
    save_button_xpath = "//span[normalize-space()='Save']//i[@class='icon-chevron-right right']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # clicking signup link function
    def clickSignupLink(self):
        self.driver.find_element_by_xpath(self.signup_link_xpath).click()

    # Entering email function
    def enterEmail(self, login_email):
        email_element = self.driver.find_element(By.ID, self.login_email_textbox_id)
        email_element.clear()
        email_element.send_keys(login_email)

    # Entering password function
    def enterPassword(self, login_password):
        password_element = self.driver.find_element(By.ID, self.login_password_textbox_id)
        password_element.clear()
        password_element.send_keys(login_password)

    # clicking signin button function
    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.login_signin_button_id).click()

    # clicking  my address button function
    def click_my_address(self):
        self.driver.find_element(By.XPATH, self.my_address_button_xpath).click()

    # clicking add new button function
    def click_add_new_button(self):
        self.driver.find_element(By.XPATH, self.add_new_address_button_xpath).click()

    # Entering first name function
    def enter_firstname(self, firstname):
        firstname_element = self.driver.find_element(By.ID, self.firstname_textbox_id)
        firstname_element.clear()
        firstname_element.send_keys(firstname)

    # Entering last name function
    def enter_lastname(self, lastname):
        lastname_element = self.driver.find_element(By.ID, self.lastname_textbox_id)
        lastname_element.clear()
        lastname_element.send_keys(lastname)

    # Entering company name function
    def enter_company_name(self, company):
        company_element = self.driver.find_element(By.ID, self.company_textbox_id)
        company_element.clear()
        company_element.send_keys(company)

    # Entering address function
    def enter_address(self, address1):
        address_element = self.driver.find_element(By.ID, self.address_textbox_id)
        address_element.clear()
        address_element.send_keys(address1)

    # Entering address(line2) function
    def enter_address_line2(self, address2):
        address2_element = self.driver.find_element(By.ID, self.address_line2_textbox_id)
        address2_element.clear()
        address2_element.send_keys(address2)

    # Entering city function
    def enter_city(self, city):
        city_element = self.driver.find_element(By.ID,self.city_textbox_id)
        city_element.clear()
        city_element.send_keys(city)

    # Selecting state function
    def select_state(self, state):
        select_state_element = self.driver.find_element(By.ID, self.state_select_id)
        select_state = Select(select_state_element)
        select_state.select_by_visible_text(state)

    # Entering pin code function
    def enter_postal_code(self, pin):
        postal_code_element = self.driver.find_element(By.ID, self.pin_code_textbox_id)
        postal_code_element.clear()
        postal_code_element.send_keys(pin)

    # Entering home phone function
    def enter_home_phone(self, phone):
        phone_element = self.driver.find_element(By.ID, self.home_phone_textbox_id)
        phone_element.clear()
        phone_element.send_keys(phone)

    # Entering mobile number function
    def enter_mobile_phone(self, mobile):
        mobile_element = self.driver.find_element(By.ID, self.mobile_textbox_id)
        mobile_element.clear()
        mobile_element.send_keys(mobile)

    # Entering additional info function
    def enter_additional_info(self, info):
        information_element = self.driver.find_element(By.ID, self.additional_information_textarea_id)
        information_element.clear()
        information_element.send_keys(info)

    # Entering address alias function
    def enter_address_alias(self, alias):
        alias_element = self.driver.find_element(By.ID, self.alias_name_textbox_id)
        alias_element.clear()
        alias_element.send_keys(alias)

    # clicking  save button function
    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, self.save_button_xpath)
        save_button.click()


