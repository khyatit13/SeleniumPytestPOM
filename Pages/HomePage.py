import time

from Pages.BasePage import BasePage

import logging

from Pages.NewCarsPage import NewCarsPage
from utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)
class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def goToNew_cars(self):
        log.logger.info("Entered goToNew_cars")
        self.mousehover("XPATH",  "newcar_XPATH")
        self.click("XPATH", "findNewCars_XPATH")
        time.sleep(5)
        return NewCarsPage(self.driver)

    def goToCompareCars(self):
        pass

    def goToUsedCars(self):
        pass