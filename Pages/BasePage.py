from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities import configReader
import logging
from utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def locator_type(self,type):
        if type=="ID":
            return By.ID
        if type=="XPATH":
            return By.XPATH
        if type=="CSS":
            return By.CSS_SELECTOR
        if type=="NAME":
            return By.NAME

    def click(self,locator_name,locator):
        self.driver.find_element(self.locator_type(locator_name), configReader.readConfig("locator", locator)).click()
        log.logger.info("Clicking on the element"+str(locator))


    def sendkeys(self,locator_name,locator,value):
        self.driver.find_element(self.locator_type(locator_name),configReader.readConfig("locator",locator)).send_keys(value)
        log.logger.info("Typing on the element" + str(locator)+"value entered as"+str(value))

    def select(self,locator_name,locator,value):
        dropdown=self.driver.find_element(self.locator_type(locator_name), configReader.readConfig("locator", locator))
        select=Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Selecing on the element" + str(locator) + "value entered as" + str(value))

    def mousehover(self,locator_name,locator):
        log.logger.info("Reached Mouse hover")
        action = ActionChains(self.driver)
        log.logger.info("Next Step is to find element")
        # element = self.driver.find_element(self.locator_type(locator_name), configReader.readConfig("locator",locator))
        element=self.driver.find_element(self.locator_type(locator_name),configReader.readConfig("locator",locator))
        log.logger.info(element)


        action.move_to_element(element).perform()

        log.logger.info("Moving to an element" +str(locator))

    def gettext(self,locator_name,locator):

        text_value=self.driver.find_element(self.locator_type(locator_name),configReader.readConfig("locator",locator)).text
        return text_value

    def getelementstext(self, locator_name1, locator1,locator_name2,locator2):


        text_value1 = self.driver.find_elements(self.locator_type(locator_name1),configReader.readConfig("locator", locator1))

        text_value2 = self.driver.find_elements(self.locator_type(locator_name2),configReader.readConfig("locator", locator2))
        log.logger.info("entered get elements")
        # print(text_value1)
        # print(text_value2)
        for i in range(0,len(text_value1)-1):
            print(text_value1[i].text +"prices :"+text_value2[i].text)
            log.logger.info("entered for loop")




