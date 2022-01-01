import json
from Utilities.customLogger import LogGen

logger=LogGen.loggen(name="Utility")

class ReadConfig:
    @staticmethod
    def GetBaseurl(configfile):
        with open(configfile,"r") as url:
            Baseurl = json.load(url)
            print(Baseurl)
            # print(Baseurl["common_info"].get("Base_Url"))
            logger.info(f'Requested base_url : {Baseurl["common_info"].get("Base_Url")}')
            return(Baseurl["common_info"].get("Base_Url"))
    
    @staticmethod
    def GetUsername(configfile):
        with open(configfile,"r") as name:
            user_name = json.load(name)
            # print(Baseurl["common_info"].get("Base_Url"))
            logger.info(f'Requested User_name : {user_name["common_info"].get("User_name")}')
            return(user_name["common_info"].get("User_name"))
    
    @staticmethod
    def GetPassword(configfile):
        with open(configfile,"r") as pas:
            password = json.load(pas)
            # print(Baseurl["common_info"].get("Base_Url"))
            logger.info(f'Requested Password : {password["common_info"].get("Password")}')
            return(password["common_info"].get("Password"))

    # @staticmethod
    # def GetChromeValidators(configfile):
    #     with open(configfile,"r") as vali:
    #         validator_1 = json.load(vali)
    #         logger.info(f'Requested validator : {validator_1["chrome_details"].get("test_case_1")}')
    #         return(validator_1["chrome_details"].get("test_case_1"))
