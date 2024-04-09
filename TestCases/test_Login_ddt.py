import time

from PageObjects.LoginPagetest import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtil

# Class Name should be start with 'Test_
class Test_001_ddt_Login:
    baseUrl = ReadConfig.get_Application_URL()
    path = r".//TestData/LoginData.xlsx"

    # log object
    log = LogGen.loggen()

    def test_Login_ddt(self, setup):
        self.log.info("=========test_001_ddt_Login=========")
        self.log.info("=========Verifying Login ddt Test=========")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.log.info("=========Application Launched=========")
        self.lp = Login(self.driver)

        self.rows= ExcelUtil.getRowCount(self.path, 'Sheet1')
        print("No of Rows: ",self.rows)

        lst_status=[] # Empty list

        for r in range(2,self.rows+1):
            self.user=ExcelUtil.readData(self.path,'Sheet1', r, 1)
            self.password=ExcelUtil.readData(self.path,'Sheet1', r, 2)
            self.exp = ExcelUtil.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            print(act_title)
            exp_title = "Dashboard / nonCommerce administration"
            if act_title == exp_title:
                if self.exp=='Pass':
                    self.log.info("=========Logging test Passed =========" )
                    try:
                        self.lp.clickLogout()
                    except ValueError:
                        print("Leave the site")
                        time.sleep(1)
                        continue
                    lst_status.append("Pass")

                elif self.exp=='Fail':
                    self.log.info("=========Logging test Failed =========")
                    try:
                        self.lp.clickLogout()
                    except ValueError:
                        print("Leave the site")
                        time.sleep(1)
                        continue
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp =='Pass':
                    self.log.info("=========Logging test Failed =========" )
                    try:
                        self.lp.clickLogout()
                    except ValueError:
                        print("Leave the site")
                        time.sleep(1)
                        continue
                    lst_status.append("Fail")

                elif self.exp=='Fail':
                    self.log.info("=========Logging test Passed =========")
                    try:
                        self.lp.clickLogout()
                    except ValueError:
                        print("Leave the site")
                        time.sleep(1)
                        continue
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.log.info("=========Logging DDT test Passed =========")
         #   self.driver.close()
            assert True
        else:
            self.log.info("=========Logging test Failed =========")
            self.driver.close()
            assert False
          #  self.driver.close
            assert False


# Run the test case from the Terminal: pytest -m -s TestCases/test_Login.py

# pytest -s -v -n=3 --html=Reports\report.html TestCases/test_Login.py --browser chrome
