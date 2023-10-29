import time

import pytest

from pages.addcontact import Contacts
from pages.basepage import BasePage
from utils import read_data
import logging


class Contact(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.c = Contacts(driver)

    def add_contact_page(self, data_key):
        data = read_data()[data_key]
        self.c.add_newcontact()
        self.c.first_name(data["fname"])
        self.c.last_name(data["lname"])
        self.c.date_of_birth(data["dob"])
        self.c.email(data["email"])
        self.c.phone_number(data["phone_number"])
        self.c.Street_Address1(data["adress1"])
        self.c.Street_Address2(data["adress2"])
        self.c.city(data["city"])
        self.c.state(data["state"])
        self.c.postal_code(data["post_code"])
        self.c.country(data["country"])
        self.c.click_submit()
        time.sleep(7)

    def add_contact_page1(self):
        self.add_contact_page("data1")

    def add_contact_page2(self):
        self.add_contact_page("data2")

    def add_contact_page3(self):
        self.add_contact_page("data3")

    def test_validate_contact_details(self):
        data2 = read_data()
        data = data2["data1"]
        self.c.click_contact_details()
        time.sleep(5)

        assert self.c.get_first_name() == data["fname"]
        assert self.c.get_last_name() == data["lname"]
        assert self.c.get_dob() == data["dob"]
        assert self.c.get_email() == data["email"]
        assert self.c.get_phone_number() == data["phone_number"]
        assert self.c.get_address1() == data["adress1"]
        assert self.c.get_address2() == data["adress2"]
        assert self.c.get_city() == data["city"]
        assert self.c.get_post_code() == data["post_code"]
        assert self.c.get_state() == data["state"]
        assert self.c.get_country() == data["country"]

    def test_delete(self):
        self.c.return_to_contact_list()
        self.c.click_table()
