from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from utilities import configReader
class Registration(BasePage):

    def __init__(self,driver):
        super().__init__(driver)




    def fillForm(self,name,phone,email,country,city,username,password):
        self.sendkeys("XPATH","name_XPATH",name)
        self.sendkeys("XPATH", "phone_XPATH", phone)
        self.sendkeys("XPATH","email_XPATH",email)
        self.select("XPATH","country_XPATH",country)
        self.sendkeys("XPATH","city_XPATH",city)
        self.sendkeys("XPATH","username_XPATH",username)
        self.sendkeys("XPATH","password_XPATH",password)
        self.click("XPATH","submit_XPATH")


