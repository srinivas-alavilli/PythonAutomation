import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    lnkCustmers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustmers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    btnSave_xpath = "//button[@name='save']"

    rdbMale_xpath = "//input[@id='Gender_Male']"
    rdbFemale_xpath = "//input[@id='Gender_Female']"

    iptEmail_xpath = "//input[@id='Email']"
    iptPassword_xpath = "//input[@id='Password']"
    iptFirstName_xpath = "//input[@id='FirstName']"
    iptLastName_xpath = "//input[@id='LastName']"
    iptDOB_xpath = "//input[@id='DateOfBirth']"
    iptCompany_xpath = "//input[@id='Company']"

    drpRoles_xpath = "//*[@id='SelectedCustomerRoleIds']/.."
    drpRoleRegistered_xpath = "//option[contains(text(), 'Registered')]"
    optRoleRegistered_xpath = "//span[contains(text(), 'Registered')]/following-sibling::span"
    drpRoleGuest_xpath = "//option[contains(text(), 'Guests')]"

    iptRegDateTo_xpath = "//input[@id='SearchRegistrationDateTo']"
    iptActDateFrom_xpath = "//input[@id='SearchLastActivityFrom']"
    iptActDateTo_xpath = "//input[@id='SearchLastActivityTo']"

    iptIpAddress_xpath = "//input[@id='SearchIpAddress']"

    drpBirthMonth_xpath = "//*[@id='SearchMonthOfBirth']"
    drpBirthDay_xpath = "//*[@id='SearchDayOfBirth']"


    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustmers_menu_xpath).click()

    def clickCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustmers_menuitem_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.iptEmail_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.iptPassword_xpath).send_keys(pwd)

    def setFirstName(self, Fname):
        self.driver.find_element(By.XPATH, self.iptFirstName_xpath).send_keys(Fname)

    def setLastName(self, Lname):
        self.driver.find_element(By.XPATH, self.iptLastName_xpath).send_keys(Lname)

    def setMale(self):
        self.driver.find_element(By.XPATH, self.rdbMale_xpath).click()

    def setFemale(self):
        self.driver.find_element(By.XPATH, self.rdbFemale_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.iptDOB_xpath).send_keys(dob)

    def setCompany(self, cmp):
        self.driver.find_element(By.XPATH, self.iptCompany_xpath).send_keys(cmp)

    def setRole(self, role):
        self.driver.find_element(By.XPATH, self.drpRoles_xpath).click()
        time.sleep(2)
        if role == 'Guests':
            self.driver.find_element(By.XPATH, self.optRoleRegistered_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.drpRoles_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.drpRoleGuest_xpath).click()
        elif role == 'Registered':
            print("No role")
            #  self.driver.find_element(By.XPATH, self.drpRoleRegistered_xpath).click()


    def setGender(self, gender):
        if gender == 'male':
            self.driver.find_element(By.XPATH, self.rdbMale_xpath).click()
        elif gender == 'female':
            self.driver.find_element(By.XPATH, self.rdbFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdbMale_xpath).click()








