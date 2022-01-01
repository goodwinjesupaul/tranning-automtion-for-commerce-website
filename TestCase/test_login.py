import pytest
from PageObject.LoginPageFrame import LoginTest
import time
from datetime import datetime
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from conftest import browser

class Test_001:
    logger=LogGen.loggen(name="Test_01")
    
    @pytest.fixture(autouse=True)
    def _request_test_details(self, configfile,get_test_details):
        self.Base_Url = ReadConfig.GetBaseurl(configfile)
        self.User_name = ReadConfig.GetUsername(configfile)
        self.Password = ReadConfig.GetPassword(configfile)
        self.test_details =get_test_details 

        # self.chrome_validator = ReadConfig.GetChromeValidators(configfile)      
    
    def test_login_page_title(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.driver.get(self.Base_Url)
        actual_tilte= self.driver.title
        # print(self.chrome_validator)
        if self.test_details["test_case_1"]["title_name"] in actual_tilte:
            assert True
            self.logger.info("****Home page title test passed****")
        else:
            tnow = str(datetime.utcnow()).split()[1]
            print(tnow)
            name = "error_{}.png".format(time.strftime("%Y-%m-%d %H_%M_%S", time.gmtime()).split()[1])
            print(name)
            self.driver.save_screenshot(".\\ScreenShot\\"+name)
            self.logger.error("****Home page title test failed****")
            assert False
        self.driver.close()
        
        

    def test_login(self,setup,):
        self.logger.info("************** test login began **************")
        self.driver = setup
        self.driver.get(self.Base_Url)
        self.lp = LoginTest(self.driver)
        self.lp.get_user_id(self.User_name)
        self.lp.get_password(self.Password)
        self.lp.click_login()
        actual_title1= self.driver.title
        time.sleep(3)       
        self.driver.close()
        print(actual_title1)
        assert actual_title1 in self.test_details["test_case_2"]["title_name"],self.logger.error(f"Actual Title is not same as:  {actual_title1}")






