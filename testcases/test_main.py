import time
import pytest

from testcases.test_contact import Contact
from testcases.test_base import BaseTest
from testcases.test_login_page import TestLogin
from utils import read_data


@pytest.mark.usefixtures
class Testherokuapp(BaseTest):

    @pytest.fixture
    def class_objects(self):
        self.lp = TestLogin(self.driver)
        self.cd = Contact(self.driver)

    @pytest.mark.usefixtures
    def test_login(self, class_objects):
        self.lp.test_home_page()
        self.lp.test_login_page()

    def test_contact_details(self, class_objects):
        self.cd.add_contact_page1()
        self.cd.add_contact_page2()
        self.cd.add_contact_page3()

    def test_contact(self, class_objects):
        self.cd.test_validate_contact_details()

    def test_delete(self, class_objects):
        self.cd.test_delete()
