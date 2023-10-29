from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

from testcases.test_base import BaseTest
from selenium.webdriver.common.by import By


class BasePage(BaseTest):

    def __init__(self, driver):
        self.driver = driver

