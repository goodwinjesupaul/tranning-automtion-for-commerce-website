# from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys

class LoginTest:
    logger = LogGen.loggen(name = "Login_Page_object")
    Text_box_User_Id = "Email"
    Text_box_Password = "Password"
    Button_Login ="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"  
    # "//button[@name='login']"
    Button_Logout = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver = driver
        self.logger.info("********* Driver recieved ***********")
        # return driver

    def get_user_id(self,user_id):
        self.logger.info("clearing text_box_user_id")
        self.driver.find_element(By.ID,self.Text_box_User_Id).clear()
        self.logger.info("passing user_id")
        self.driver.find_element(By.ID,self.Text_box_User_Id).send_keys(user_id)

    def get_password(self,password):
        self.logger.info("clearing pasword_text_box")
        self.driver.find_element(By.ID,self.Text_box_Password).clear()
        self.logger.info("passing password")
        self.driver.find_element(By.ID,self.Text_box_Password).send_keys(password)

    def click_login(self):
        self.logger.info("selecting login_in_button")
        self.driver.find_element(By.XPATH,self.Button_Login).click()
        
    def clickLogout(self):
        self.logger.info("selecting login_out_button")
        self.driver.find_element(By.XPATH,self.Button_Logout).click()        