import pytest

from PageObjects.LoginPagetest import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

# Class Name should be start with 'Test_
class Test_001_Login:
    baseUrl = ReadConfig.get_Application_URL()
    username = ReadConfig.get_UserName()
    password = ReadConfig.get_Password()
    # log object
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_HomePageTitle(self, setup):
        self.log.info("=========test_001_Login=========")
        self.log.info("=========Validating the HomePage Title=========")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.log.info("=========Application Launched=========")
        act_title = self.driver.title

        print(act_title)
        if act_title == "Your store. Login":
            self.log.info("=========HomePage title test Passed =========" + act_title)
            self.driver.close()
            assert True
        else:
            self.log.info("=========HomePage title test Failed =========" + act_title)
            self.driver.save_screenshot(r".\\ScreenShots\\"+ HomePageTitle.png)
            self.driver.close
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Login(self, setup):
        self.log.info("=========test_001_Login=========")
        self.log.info("=========Validating the Login=========")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.log.info("=========Application Launched=========")

        self.lp = Login(self.driver)

        self.lp.setUserName(self.username)
        self.log.info("=========Entered username =========" + self.username)
        self.lp.setPassword(self.password)
        self.log.info("=========Entered password =========" + self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        print(act_title)
        if act_title == "DashBoard":
            self.log.info("=========DashBoard title test Passed =========" + act_title)
            self.driver.close()
            assert True
        else:
            self.log.info("=========DashBoard title test Failed =========" + act_title)
            self.driver.save_screenshot(".\\ScreenShots\\" + Login.png)
            self.driver.close
            assert False  # Run the test case from the Terminal: pytest -m -s TestCases/test_Login.py


# pytest -s -v -n=3 --html=Reports\report.html TestCases/test_Login.py --browser chrome
