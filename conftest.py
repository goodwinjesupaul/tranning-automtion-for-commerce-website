from selenium import webdriver
import pytest
from Utilities.customLogger import LogGen
import json
logger=LogGen.loggen(name=__name__)


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Goodwin/Documents/FaceBookApp/TestCase/chromedriver.exe")
        logger.info("created chrome driver")  
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:/Users/Goodwin/Documents/FaceBookApp/TestCase/geckodriver.exe")
        logger.info("created firefox driver")  
    return driver

@pytest.fixture()
def get_test_details(browser,configfile):
    if browser=="chrome":
        logger.info("Getting test details for chrome")
        with open(configfile,"r",encoding= "utf-8") as vali:
            validator_1 = json.load(vali)
            logger.info(f'Requested validator : {validator_1["chrome_details"]}')
            return(validator_1["chrome_details"])
    elif browser == "firefox":
        with open(configfile,"r") as vali:
            logger.info("Getting test details for firefox")  
            validator_1 = json.load(vali)
            logger.info(f'Requested validator : {validator_1["firefox_details"]}')
            return(validator_1["firefox_details"])

@pytest.fixture()
def browser(request):
    browser_path =request.config.getoption("--browser")
    logger.info(f"Requested configfile path : {browser_path}")  
    return browser_path

def pytest_addoption(parser):
    parser.addoption("--configfile")
    parser.addoption("--browser")

@pytest.fixture()
def configfile(request):
    config_path =request.config.getoption("--configfile")
    logger.info(f"Requested configfile path : {config_path}")  
    return config_path

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Facebook'
    config._metadata['Module Name'] = 'Learning'
    config._metadata['Tester'] = 'Goodwin'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)