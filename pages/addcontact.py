import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.basepage import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


class Contacts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_and_send(self, element_id, value):
        self.driver.find_element(By.ID, element_id).send_keys(value)

    def find_and_click(self, element_id):
        self.driver.find_element(By.ID, element_id).click()

    def set_find_xpath_click(self, element_xpath):
        self.driver.find_element(By.XPATH, element_xpath).click()

    def add_newcontact(self):
        self.find_and_click("add-contact")

    def first_name(self, fname):
        self.find_and_send("firstName", fname)

    def last_name(self, lname):
        self.find_and_send("lastName", lname)

    def date_of_birth(self, dob):
        self.find_and_send("birthdate", dob)

    def phone_number(self, pnumber):
        self.find_and_send("phone", pnumber)

    def email(self, email):
        self.find_and_send("email", email)

    def Street_Address1(self, address):
        self.find_and_send("street1", address)

    def Street_Address2(self, address2):
        self.find_and_send("street2", address2)

    def city(self, city):
        self.find_and_send("city", city)

    def state(self, state):
        self.find_and_send("stateProvince", state)

    def postal_code(self, pcode):
        self.find_and_send("postalCode", pcode)

    def country(self, country):
        self.find_and_send("country", country)

    def click_submit(self):
        self.find_and_click("submit")

    def click_table(self):
        while True:
            try:
                self.set_find_xpath_click("//tr[1]//td[3]")
                self.find_and_click("delete")
                alert = Alert(self.driver)
                alert.accept()
            except Exception as e:
                break

    def find_element_text(self, by, value):
        element = self.driver.find_element(by, value)
        return element.text

    def click_contact_details(self):
        self.set_find_xpath_click("(//td)[2]")

    def get_first_name(self):
        return self.find_element_text(By.ID, "firstName")

    def get_last_name(self):
        return self.find_element_text(By.ID, "lastName")

    def get_dob(self):
        return self.find_element_text(By.ID, "birthdate")

    def get_phone_number(self):
        return self.find_element_text(By.ID, "phone")

    def get_email(self):
        return self.find_element_text(By.ID, "email")

    def get_address1(self):
        return self.find_element_text(By.ID, "street1")

    def get_address2(self):
        return self.find_element_text(By.ID, "street2")

    def get_city(self):
        return self.find_element_text(By.ID, "city")

    def get_state(self):
        return self.find_element_text(By.ID, "stateProvince")

    def get_post_code(self):
        return self.find_element_text(By.ID, "postalCode")

    def get_country(self):
        return self.find_element_text(By.ID, "country")

    def return_to_contact_list(self):
        return_contact_list = self.driver.find_element(By.ID, "return")
        return_contact_list.click()
