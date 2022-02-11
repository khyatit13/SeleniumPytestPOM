from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

import pytest
import openpyxl

from Pages.RegistrationPage import Registration
from Testcases.BaseTest import BaseTest
from utilities.dataprovider import get_data

import logging
from utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)










class Test_Registration(BaseTest):



    @pytest.mark.parametrize("name,phone,email,country,city,username,password", get_data("LoginTest"))
    def test_dologin(self,name,phone,email,country,city,username,password):
        log.logger.info("Test Do Sign up started")

        regPage=Registration(self.driver)
        regPage.fillForm(name,phone,email,country,city,username,password)
        log.logger.info("Test Do Sign up ended")

   # assert 1 == 2
# allure.attach(driver.get_screenshot_as_png(),name="dologin",attachment_type=AttachmentType.PNG)
