import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Loginpage import loginpage
from Utilities.ReadProperties import readconfig
from Utilities.customLogger import LogGen


class Test_001_login:
    baseURL = readconfig.getApplicationURL()
    username = readconfig.getusername()
    password = readconfig.getpassword()

    logger=LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("******************Test__001__Login*****************")
        self.logger.info("*****************Verifying Home Page Title*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("****************Home Page Title Test is Passed************")
        else:
            self.driver.save_screenshot("self.d")
            self.driver.close()
            self.logger.info("****************Home Page Title Test is failed************")
            assert False

    def test_login(self,setup):
        self.logger.info("****************Verifying the Login Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.logger.info("**************** Login Test is Passed************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"testlogin.png")
            self.driver.close()
            self.logger.info("****************Login Test is failed************")
            assert False
