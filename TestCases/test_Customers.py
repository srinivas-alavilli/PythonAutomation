import random
import string
import time

import pytest

from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.LoginPagetest import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

# Class Name should be start with 'Test_
class Test_003_AddCustomer:
    baseUrl = ReadConfig.get_Application_URL()
    username = ReadConfig.get_UserName()
    password = ReadConfig.get_Password()
    # log object
    log = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.log.info("=========test_003_AddCustomer=========")
        self.log.info("=========Adding the New Customer=========")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.log.info("=========Application Launched=========")
        self.driver.maximize_window()

        self.log.info("=========Login the Application=========")

        # Objects creation
        self.lp = Login(self.driver)
        self.ac = AddCustomer(self.driver)

        # Logging the application
        self.lp.setUserName(self.username)
        self.log.info("=========Entered username =========" + self.username)
        self.lp.setPassword(self.password)
        self.log.info("=========Entered password =========" + self.password)
        self.lp.clickLogin()
        self.log.info("=========Login Successful =========")

        # Adding the Customer
        self.log.info("=========Started Adding the Customer =========")
        self.ac.clickCustomerMenu()
        self.ac.clickCustomerMenuItem()

        self.log.info("=========Giving Customer Info =========")
        self.ac.clickAddNew()

        self.email="esfsdaf@customer.com"
        self.ac.setEmail(self.email)

        self.ac.setPassword('pass123')
        self.ac.setFirstName('SriTest')
        self.ac.setLastName('SriTest')
        self.ac.setDOB('03/02/2001')
        self.ac.setGender('male')
        self.ac.setRole('Registered')
        self.ac.setCompany('SriLtd')
        self.ac.clickSave()
        time.sleep(5)
        self.log.info("=========Saved the Customer Info =========")

    # def test_random_generator(size = 8):
    #     ran = ''.join(random.choice(string.ascii_lowercase+string.digits), size)
    #     # ran = ''.join(random.choices(chars) for x in range(size))
    #     return ran
    #     print("The randomly generated string is : " + str(ran))  # print the random data
    #     # S = 10  # number of characters in the string.
    #     # # call random.choices() string module to find the string in Uppercase + numeric data.
    #     # ran = ''.join(random.choices(string.ascii_uppercase+string.digits, k = S))

# pytest -s -v -n=1 --html=Reports\report.html TestCases/test_Customers.py --browser chrome

# To run all test cases under TestCases Package -------
# pytest -s -v -n=1 --html=Reports\report.html TestCases/ --browser chrome

# To run tests by group by using 'markers' like sanity or regression  -------
# pytest -s -v -m "sanity" -n=1 --html=Reports\report.html TestCases/ --browser chrome
