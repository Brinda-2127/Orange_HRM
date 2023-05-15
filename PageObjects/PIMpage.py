import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage_001:
    link_pim_xpath = "//span[text()='PIM']"
    link_addEmployee_xpath = "//a[text()='Add Employee']"
    text_firstname_xpath = "//input[@name='firstName']"
    text_MidName_xpath = "//input[@name='middleName']"
    text_lastname_xpath = "//input[@name='lastName']"
    btn_submit_xpath = "//button[@type='submit']"
    btn_CreateLogin_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    text_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    text_password_xpath = "(//input[@type='password'])[1]"
    button_enabled_xpath = "//label[normalize-space()='Enabled']"
    text_CnfrmPasswrd_xpath = "(//input[@type='password'])[2]"
    btn_save_xpath = "//button[@type='submit']"
    link_P_detail_xpath = "//a[text()='Personal Details']"
    txt_N_name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    txt_Emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    txt_other_id_xpath = "//label[text()='Other Id']//parent::div//following-sibling::div//input"
    txt_L_E_date_xpath = "//label[contains(text(),'License Expiry Date')]//parent::div//following-sibling::div//input"
    txt_Driver_lc_xpath = "//label[contains(text(),'License Number')]//parent::div//following-sibling::div//input"
    txt_ssn_xpath = "//label[contains(text(),'SSN Number')]//parent::div//following-sibling::div//input"
    txt_sin_xpath = "//label[contains(text(),'SIN Number')]//parent::div//following-sibling::div//input"
    txt_M_service_xpath = "//label[contains(text(),'Military Service')]//parent::div//following-sibling::div//input"
    drp_nationality_xpath = "//label[contains(text(),'Nationality')]//parent::div//following-sibling::div//div[@class='oxd-select-wrapper']"
    drp_M_Status_xpath = "//label[contains(text(),'Marital Status')]//parent::div//following-sibling::div//div[@class='oxd-select-wrapper']"
    txt_dob_xpath = "//label[contains(text(),'Date of Birth')]//parent::div//following-sibling::div//input"
    rd_MaleGender_xpath = "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]"
    rd_femaleGender_xpath = "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]"
    btn_PD_save_xpath = "(//button[@type='submit'])[1]"
    drp_bl_group_xpath = "//label[contains(text(),'Blood Type')]//parent::div//following-sibling::div//div[@class='oxd-select-wrapper']"
    btn_customSave_xpath = "(//button[@type='submit'])[2]"
    btn_add_attachment_xpath = "//h6[text()='Attachments']//parent::div//following-sibling::button"
    btn_customerFields_xpath = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']"
    btn_browse_xpath = "//div[@class='oxd-file-button']"
    txt_type_comment_xpath = "//label[contains(text(),'Comment')]//parent::div//following-sibling::div//textarea"
    btn_after_attach_save_xpath = "(//button[@type='submit'])[3]"
    txt_E_name_xpath = "(//input[@placeholder='Type for hints...'])[1]"
    btn_search_xpath = "//button[@type='submit']"
    btn_edit_xpath = "//i[@class='oxd-icon bi-pencil-fill']"
    btn_delete_xpath = "//i[@class='oxd-icon bi-trash']"
    btn_checkbox_xpath="(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def clickPIM_menu(self):
        self.driver.find_element(By.XPATH, self.link_pim_xpath).click()

    def clickAddEmployee(self):
        self.driver.find_element(By.XPATH, self.link_addEmployee_xpath).click()

    def setFirstName(self, f_name):
        self.driver.find_element(By.XPATH, self.text_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_firstname_xpath).send_keys(f_name)

    def setMiddleName(self, M_name):
        self.driver.find_element(By.XPATH, self.text_MidName_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_MidName_xpath).send_keys(M_name)

    def setLastName(self, l_name):
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).send_keys(l_name)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_CreateLogin_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def setConfirmPassword(self, C_Password):
        self.driver.find_element(By.XPATH, self.text_CnfrmPasswrd_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_CnfrmPasswrd_xpath).send_keys(C_Password)

    def ClickEnable(self):
        self.driver.find_element(By.XPATH, self.button_enabled_xpath).click()

    def ClickSaveDetail(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ClickPersonalDetail(self):
        self.driver.find_element(By.XPATH, self.link_P_detail_xpath).click()

    def setNickname(self, N_name):
        self.driver.find_element(By.XPATH, self.txt_N_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_N_name_xpath).send_keys(N_name)

    # def setEmployee_Id(self,number):
    #     self.driver.find_element(By.XPATH, self.txt_Emp_id_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_Emp_id_xpath).send_keys(number)

    def setOther_id(self, number):
        # self.WebDriverWait.until((EC.presence_of_element_located((By.XPATH, self.txt_other_id_xpath)))).send_keys(number)
        self.driver.find_element(By.XPATH, self.txt_other_id_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_other_id_xpath).send_keys(number)

    def setDriving_license(self, number):
        self.driver.find_element(By.XPATH, self.txt_Driver_lc_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_Driver_lc_xpath).send_keys(number)

    def setDrivingLicenceEx_date(self, date):
        self.driver.find_element(By.XPATH, self.txt_L_E_date_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_L_E_date_xpath).send_keys(date)

    def setSSN_Num(self, number):
        self.driver.find_element(By.XPATH, self.txt_ssn_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_ssn_xpath).send_keys(number)

    def setSIN_Num(self, number):
        self.driver.find_element(By.XPATH, self.txt_sin_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_sin_xpath).send_keys(number)

    def setNationality(self, nation):
        element = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]").text
        while text1 != nation:
            element.send_keys(Keys.ARROW_DOWN)
            text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]").text
        self.driver.find_element(By.XPATH, self.drp_nationality_xpath).click()

    def setMarital_Status(self, status):
        element = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").text
        while text1 != status:
            element.send_keys(Keys.ARROW_DOWN)
            text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").text
        self.driver.find_element(By.XPATH, self.drp_M_Status_xpath).click()

    def setDOB(self, date):
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(date)

    def setGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.XPATH, self.rd_MaleGender_xpath).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.XPATH, self.rd_femaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_MaleGender_xpath).click()

    def setMilitary_Service(self, number):
        self.driver.find_element(By.XPATH, self.txt_M_service_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_M_service_xpath).send_keys(number)

    def ClickSaveP_detail(self):
        self.driver.find_element(By.XPATH, self.btn_PD_save_xpath).click()

    def setBloodGroup(self, Type):
        element = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]")
        text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]").text
        while text1 != Type:
            element.send_keys(Keys.ARROW_DOWN)
            text1 = self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]").text
        self.driver.find_element(By.XPATH, self.drp_bl_group_xpath).click()

    def ClickCustomSave(self):
        self.driver.find_element(By.XPATH, self.btn_customSave_xpath).click()

    # def setCustom_Field(self):
    # self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, self.btn_customerFields_xpath)))

    def Click_Add_Attachment(self):
        # self.WebDriverWait.until((EC.presence_of_element_located((By.XPATH, self.btn_add_attachment_xpath))))
        self.driver.find_element(By.XPATH, self.btn_add_attachment_xpath).click()
        time.sleep(3)

    def upload_file(self):
        # self.driver.find_element(By.XPATH, self.btn_browse_xpath).send_keys(self.file_xpath)
        element = self.driver.find_element(By.XPATH, self.btn_browse_xpath)
        file_xpath = "F://Jaga's//OneDrive//Jaga's//Desktop"
        self.driver.execute_script("arguments[0].value = arguments[1];", element, file_xpath)
        # self.driver.find_element(By.CSS_SELECTOR, ".oxd-file-button").send_keys("C://fakepath//Test.txt")

    def set_comment(self):
        self.driver.find_element(By.XPATH, self.txt_type_comment_xpath).send_keys("comment")

    def ClickSave_all(self):
        self.driver.find_element(By.XPATH, self.btn_after_attach_save_xpath).click()

    def getText(self):
        element = self.driver.find_element(By.XPATH, "//div[@id='oxd-toaster_1']")

        # Get the text of the WebElement using JavaScript executor
        text = self.driver.execute_script("return arguments[0].textContent;", element)
        print("Element text:", text)

    def setEmployee_name(self, name):
        # self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, self.txt_E_name_xpath))).send_keys(name)
        self.driver.find_element(By.XPATH, self.txt_E_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_E_name_xpath).send_keys(name)

    def Click_search(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def ClickEdit(self):
        self.driver.find_element(By.XPATH,self.btn_edit_xpath).click()

    def ClickCheckbox(self):
        self.driver.find_element(By.XPATH,self.btn_checkbox_xpath).click()

    def ClickDeleteIcon(self):
        self.driver.find_element(By.XPATH,self.btn_delete_xpath).click()


