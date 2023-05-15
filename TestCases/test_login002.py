import pytest
from PageObjects.Loginpage import loginpage
from Utilities.ReadProperties import readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DDT_Login:
    logger = LogGen.loggen()  # Logger

    # @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("******* Starting Valid_login Test **********")
        self.driver = setup
        self.lp = loginpage(self.driver)
        self.username = readconfig.getusername().strip()
        self.password = readconfig.getpassword().strip()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clicklogin()
        time.sleep(5)
        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            self.logger.info("******* Valid_login test passed **********")
            self.lp.clicklogout()
            assert True
        else:
            self.logger.error("******* Valid_login test failed **********")
            assert False

        self.logger.info("**************** Completed  TC_Login_Valid_login_Test ************* ")
        self.driver.close()

    def test_Invalid_login(self, setup):
        self.logger.info("******* Starting Invalid_Valid_login Test **********")
        self.driver = setup
        self.lp = loginpage(self.driver)
        self.username = readconfig.get_invalid_username().strip()
        self.password = readconfig.get_invalid_password().strip()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clicklogin()
        time.sleep(5)
        act_alert_msg = "Invalid credentials"
        exp_alert_msg = self.lp.invalid_alert()
        print(exp_alert_msg)
        if act_alert_msg == exp_alert_msg:
            self.logger.info("******* Invalid_login_test passed **********")
            assert True

        else:
            self.logger.error("******* Invalid_Login test failed **********")
            assert False
        self.logger.info("**************** Completed  Invalid_login_Test************ ")
        self.driver.close()
