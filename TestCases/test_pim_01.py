import time
import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Loginpage import loginpage
from Utilities.ReadProperties import readconfig
from Utilities.customLogger import LogGen
from PageObjects.PIMpage import PIMPage_001
from Utilities import XLUtils


class Test_PIM_001:
    path = ".//TestData/orangehrmdata.xlsx"
    logger = LogGen.loggen()

    def test_personal_detail(self, setup):
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
        self.PIM.clickAddEmployee()
        self.logger.info("*****Go to PIM Add Employee Page*******")
        self.logger.info("*****providing information*******")

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)

        for r in range(2, self.rows + 1):
            self.f_name = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.M_name = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.l_name = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.user_name = XLUtils.readData(self.path, 'Sheet1', r, 4)
            self.P_word = XLUtils.readData(self.path, 'Sheet1', r, 5)
            self.CP_word = XLUtils.readData(self.path, 'Sheet1', r, 6)

            self.PIM.setFirstName(self.f_name)
            self.PIM.setMiddleName(self.M_name)
            self.PIM.setLastName(self.l_name)
            self.PIM.ClickLogin()
            time.sleep(3)
            self.PIM.setUserName(self.user_name)
            self.PIM.setPassword(self.P_word)
            self.PIM.setConfirmPassword(self.CP_word)
            self.PIM.clickSave()
            time.sleep(10)
            self.logger.info("sucessfully come to pesonal Details")

        self.rows1 = XLUtils.getRowCount(self.path, 'Sheet2')
        print('Number of rows...', self.rows1)
        for r1 in range(2, self.rows1 + 1):
            self.N_name = XLUtils.readData(self.path, 'Sheet2', r1, 1)
            self.Other_ID = XLUtils.readData(self.path, 'Sheet2', r1, 2)
            self.DL_num = XLUtils.readData(self.path, 'Sheet2', r1, 3)
            self.L_E_date = XLUtils.readData(self.path, 'Sheet2', r1, 4)
            self.SSN = XLUtils.readData(self.path, 'Sheet2', r1, 5)
            self.SIN = XLUtils.readData(self.path, 'Sheet2', r1, 6)
            self.DOB = XLUtils.readData(self.path, 'Sheet2', r1, 7)
            self.Blood_Type = XLUtils.readData(self.path, 'Sheet2', r1, 8)
            self.logger.info("*********** personal detail entry started****")

            self.PIM.setNickname(self.N_name)
            time.sleep(2)
            self.PIM.setOther_id(self.Other_ID)
            time.sleep(2)
            self.PIM.setDriving_license(self.DL_num)
            time.sleep(2)
            self.PIM.setDrivingLicenceEx_date(self.L_E_date)
            time.sleep(2)
            self.PIM.setSSN_Num(self.SSN)
            self.PIM.setSIN_Num(self.SIN)
            self.PIM.setNationality('Indian')
            self.PIM.setMarital_Status("Married")
            self.PIM.setDOB(self.DOB)
            self.PIM.setGender("female")
            self.PIM.setMilitary_Service("Active Guard")
            self.PIM.ClickSaveP_detail()
            self.logger.info("**********Personal detail message verification started****")
            self.PIM.getText()

            # Custom fields
            # self.PIM.setCustom_Field()
            self.PIM.setBloodGroup("A+")
            self.PIM.ClickCustomSave()
            self.PIM.getText()

            # Attachment Fields
            self.PIM.Click_Add_Attachment()
            time.sleep(3)
            self.PIM.upload_file()
            self.PIM.set_comment()
            self.PIM.ClickSave_all()
            self.PIM.getText()

            self.logger.info("*** Saving info ***")
            self.logger.info("*** Personal Details Validation Ended ***")
            time.sleep(10)
            self.driver.back()
            self.PIM.clickPIM_menu()
            self.PIM.setEmployee_name("manu")
            self.PIM.Click_search()
            exp_name = self.driver.find_element(By.XPATH, "//div[text()='Manu kumar']").text
            act_name = "Manu kumar"
            if exp_name == act_name:
                assert True
            else:
                assert False
        self.logger.info("******Personal detail Record Created********")
        self.driver.close()

