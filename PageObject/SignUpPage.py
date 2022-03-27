from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Signup:
    # page locator
    signup_link_xpath = "//a[@title='Log in to your customer account']"
    email_textbox_id = "email_create"
    create_button_xpath = "//span[normalize-space()='Create an account']"
    # Personal Information
    title_radio_id = "id_gender1"
    title2_radio_id = "id_gender2"
    firstname_textbox_id = "customer_firstname"
    lastname_textbox_id = "customer_lastname"
    password_textbox_id = "passwd"
    day_select_id = "days"
    month_select_id = "months"
    years_select_id = "years"
    newsletter_checkbox_id = "newsletter"
    offer_checkbox_id = "optin"
    # Address Information
    address_firstname_textbox_id = "firstname"
    address_lastname_textbox_id = "lastname"
    address_company_textbox_id = "company"
    address_textbox_id = "address1"
    address_line2_textbox_id = "address2"
    address_city_textbox_id = "city"
    address_state_select_id = "id_state"
    address_pin_code_textbox_id = "postcode"
    address_other_info_textarea_id = "other"
    address_home_phone_textbox_id = "phone"
    address_mobile_textbox_id = "phone_mobile"
    address_alias_textbox_id = "alias"
    register_button_xpath = "//span[normalize-space()='Register']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # signup link click path function
    def click_signup_link(self):
        self.driver.find_element(By.XPATH, self.signup_link_xpath).click()

    # email id text action function
    def enter_email_address(self, email):
        personal_email = self.driver.find_element(By.ID, self.email_textbox_id)
        personal_email.clear()
        personal_email.send_keys(email)

    # Create button click action function
    def click_create_an_account(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    # title clicking function
    def click_title(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, self.title_radio_id).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, self.title2_radio_id).click()
        else:
            self.driver.find_element(By.ID, self.title_radio_id).click()

    # Entering firstname in personal information section function
    def enter_personal_information_firstname(self, personal_firstname):
        personal_info_firstname = self.driver.find_element(By.ID, self.firstname_textbox_id)
        personal_info_firstname.clear()
        personal_info_firstname.send_keys(personal_firstname)

    # Entering lastname in personal information function
    def enter_personal_information_lastname(self, personal_lastname):
        personal_info_lastname = self.driver.find_element(By.ID, self.lastname_textbox_id)
        personal_info_lastname.clear()
        personal_info_lastname.send_keys(personal_lastname)

    # Entering password function
    def enter_password(self, password):
        password_element = self.driver.find_element(By.ID, self.password_textbox_id)
        password_element.clear()
        password_element.send_keys(password)

    # select data function
    def select_date_of_birth(self, day, month, year):
        drop_days = self.driver.find_element(By.ID, self.day_select_id)
        drop_day = Select(drop_days)
        drop_day.select_by_value(day)
        drop_months = self.driver.find_element(By.ID, self.month_select_id)
        months = Select(drop_months)
        months.select_by_value(month)
        drop_years = self.driver.find_element(By.ID, self.years_select_id)
        years = Select(drop_years)
        years.select_by_value(year)

    # clicking news letter checkbox function
    def click_news_letter(self):
        self.driver.find_element(By.ID, self.newsletter_checkbox_id).click()

    # clicking offer mailing checkbox function
    def click_offer_mail(self):
        self.driver.find_element(By.ID, self.offer_checkbox_id).click()

    # Entering firstname of address section function
    def enter_address_firstname(self, address_firstname):
        firstname_address = self.driver.find_element(By.ID, self.address_firstname_textbox_id)
        firstname_address.clear()
        firstname_address.send_keys(address_firstname)

    # Entering lastname of address section function
    def enter_address_lastname(self, address_lastname):
        lastname_address = self.driver.find_element(By.ID, self.address_lastname_textbox_id)
        lastname_address.clear()
        lastname_address.send_keys(address_lastname)

    # Entering company name function
    def enter_company_name(self, company):
        company_element = self.driver.find_element(By.ID, self.address_company_textbox_id)
        company_element.clear()
        company_element.send_keys(company)

    # Entering address function
    def enter_address(self, address):
        address_element = self.driver.find_element(By.ID, self.address_textbox_id)
        address_element.clear()
        address_element.send_keys(address)

    # Entering address line2 function
    def enter_address_line2(self, address2):
        address_line2 = self.driver.find_element(By.ID, self.address_line2_textbox_id)
        address_line2.clear()
        address_line2.send_keys(address2)

    # Entering city data function
    def enter_city(self, city):
        city_element = self.driver.find_element(By.ID, self.address_city_textbox_id)
        city_element.clear()
        city_element.send_keys(city)

    # selecting state function
    def select_state(self, state):
        state_element = self.driver.find_element(By.ID, self.address_state_select_id)
        drop_state = Select(state_element)
        drop_state.select_by_visible_text(state)

    # Entering pin code function
    def enter_pin_code(self, postal_code):
        pin_code = self.driver.find_element(By.ID, self.address_pin_code_textbox_id)
        pin_code.clear()
        pin_code.send_keys(postal_code)

    # Entering other information function
    def enter_other_information(self, other_information):
        other_info = self.driver.find_element(By.ID, self.address_other_info_textarea_id)
        other_info.clear()
        other_info.send_keys(other_information)

    # Entering home phone function
    def enter_home_phone(self, home_phone):
        self.driver.find_element(By.ID, self.address_home_phone_textbox_id).clear()
        self.driver.find_element(By.ID, self.address_home_phone_textbox_id).send_keys(home_phone)

    # Entering mobile number function
    def enter_mobile_number(self, mobile):
        self.driver.find_element(By.ID, self.address_mobile_textbox_id).clear()
        self.driver.find_element(By.ID, self.address_mobile_textbox_id).send_keys(mobile)

    # Entering address alias function
    def enter_address_alias(self, alias):
        self.driver.find_element(By.ID, self.address_alias_textbox_id).clear()
        self.driver.find_element(By.ID, self.address_alias_textbox_id).send_keys(alias)

    # clicking register button function
    def click_register(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()
