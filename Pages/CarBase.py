import logging

from Pages.BasePage import BasePage
from utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)
class CarBase(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    def getCarTitle(self):
        log.logger.info("entered")
        return self.gettext("XPATH","cartitle_XPATH")

    def getCarNameandPrices(self):
        self.getelementstext("XPATH","carNames_XPATH","XPATH","carPrice_XPATH")
