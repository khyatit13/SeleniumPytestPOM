import time

import pytest
import openpyxl

from Pages.CarBase import CarBase
from Pages.NewCarsPage import NewCarsPage
from Pages.RegistrationPage import Registration
from Testcases.BaseTest import BaseTest
from utilities.dataprovider import get_data
from Pages.HomePage import  HomePage

import logging
from utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)










class Test_Carwale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("@@@@@@@@@@@@@Inside New Car Test@@@@@@@@@@@")
        Home=HomePage(self.driver)
        Home.goToNew_cars()
        time.sleep(3)
    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", get_data("NewCarTest"))
    def test_SelectCars(self, carBrand,carTitle):
        log.logger.info("@@@@@@@@@@@@@Inside New CarBrand@@@@@@@@@@@")
        Home = HomePage(self.driver)
        CarTitle=CarBase(self.driver)
        print(carBrand)
        if carBrand=='BMW':
            Home.goToNew_cars().selectBMW()
            title=CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title==carTitle,"Not Found"

        elif carBrand == 'Honda':
            Home.goToNew_cars().selectHonda()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle, "Not Found"
        elif carBrand == 'Toyota':
            Home.goToNew_cars().selectToyota()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle,"Not Found"
        elif carBrand == 'Hyundai':
            Home.goToNew_cars().selectHyundai()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle, "Not Found"
        time.sleep(5)


    @pytest.mark.parametrize("carBrand,carTitle", get_data("NewCarTest"))
    def test_printcarNameandPrices(self, carBrand,carTitle):
        log.logger.info("@@@@@@@@@@@@@Inside New CarBrand@@@@@@@@@@@")
        Home = HomePage(self.driver)
        CarTitle=CarBase(self.driver)
        print(carBrand)
        if carBrand=='BMW':
            Home.goToNew_cars().selectBMW()
            title=CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title==carTitle,"Not Found"
            CarTitle.getCarNameandPrices()

        elif carBrand == 'Honda':
            Home.goToNew_cars().selectHonda()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle, "Not Found"
            CarTitle.getCarNameandPrices()
        elif carBrand == 'Toyota':
            Home.goToNew_cars().selectToyota()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle,"Not Found"
            CarTitle.getCarNameandPrices()
        elif carBrand == 'Hyundai':
            Home.goToNew_cars().selectHyundai()
            title = CarTitle.getCarTitle()
            log.logger.info(carTitle)
            assert title == carTitle, "Not Found"
            CarTitle.getCarNameandPrices()
        time.sleep(5)