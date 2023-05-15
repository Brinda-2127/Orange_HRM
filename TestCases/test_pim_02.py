import time
import pytest
import self as self
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from PageObjects.Loginpage import loginpage
from Utilities.ReadProperties import readconfig
from Utilities.customLogger import LogGen
from PageObjects.PIMpage import PIMPage_001
from Utilities import XLUtils
from selenium.webdriver.common.alert import Alert


class Test_PIM_002:
    logger = LogGen.loggen()

    def test_Edit_details(self, setup):
        self.logger.info("******* Start Login to Page **********")
        self.driver = setup
        self.lp = loginpage(self.driver)
        self.username = readconfig.getusername().strip()
        self.password = readconfig.getpassword().strip()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clicklogin()

        self.PIM = PIMPage_001(self.driver)
        self.PIM.clickPIM_menu()
        self.logger.info("*****Go to PIM Page*******")
        self.PIM.setEmployee_name("manu")
        self.PIM.Click_search()
        time.sleep(5)
        self.PIM.ClickCheckbox()
        self.PIM.ClickEdit()
        time.sleep(5)
        self.logger.info("***********Enter Into Edit page ")
        self.logger.info("*************Editing Started***********")
        self.PIM.setNickname("Manoj")
        time.sleep(2)
        self.PIM.setOther_id("678")
        time.sleep(2)
        self.PIM.setDriving_license("345435")
        time.sleep(2)
        self.PIM.setSSN_Num("343")
        self.PIM.setSIN_Num("870")
        self.PIM.ClickSaveP_detail()
        self.logger.info("*********Personal Detail Edited Successfully****************")

    def test_delete_file(self, setup):
        self.logger.info("******* Start Login to Page **********")
        self.driver = setup
        self.lp = loginpage(self.driver)
        self.username = readconfig.getusername().strip()
        self.password = readconfig.getpassword().strip()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clicklogin()

        self.PIM = PIMPage_001(self.driver)
        self.PIM.clickPIM_menu()
        self.logger.info("*****Go to PIM Page*******")
        self.PIM.setEmployee_name("manu")
        self.PIM.Click_search()
        time.sleep(5)
        self.PIM.ClickCheckbox()
        self.PIM.ClickDeleteIcon()

        try:
            alert = self.driver.switch_to.alert
            # Handle the alert here
        except NoAlertPresentException:
            # Alert not found, handle the absence of alert here
            print("No alert found.")

        self.logger.info("*******************File Successfully Deleted************")
        self.logger.info("**********Delete File Test Passed**********")
        # self.driver.quite()
