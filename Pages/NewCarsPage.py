from Pages.BasePage import BasePage

class NewCarsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def selectHyundai(self):
        self.click("XPATH","hyundai_XPATH")

    def selectToyota(self):
        self.click("XPATH","toyota_XPATH")

    def selectBMW(self):
        self.click("XPATH","bmw_XPATH")

    def selectHonda(self):
        self.click("XPATH","honda_XPATH")
