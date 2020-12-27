from behave import *
from selenium import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from decouple import config
import logging
import time
#import pyautogui
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

logging.basicConfig(level=logging.DEBUG,
                    filename="contido.log",
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filemode='a+')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
#console.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger_login= logging.getLogger('scontido_add_show.py')
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
# options=chrome_options



@given('User Launches Chrome browser')
def launchBrowser(context):
    URL_PATH = config('URL')
    wait_time = 1
    driver.implicitly_wait(4)
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(URL_PATH)



@when('User opens URL "https://dyn.stg.contido.io/login"')
def openUrl(context):
    logger_login.info("Connection created successfully")
    ''' login '''

@when('User enters Email as "opsuser@desynova.com" and Password as "dyn@opsuser20"')
def EnterCredentials(context):
    username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
    username.clear()
#   username.send_keys(config('operation_user'))
    username.send_keys('opsuser@desynova.com')
    logger_login.info("username entered")
    # time.sleep(2)
    password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
    password.clear()
#   password.send_keys('config('operation_password')')
    password.send_keys('dyn@opsuser20')
    logger_login.info("password entered")


@when('user clicks on login')
def Login(context):
    login = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
    login.click()
    logger_login.info("login successfull")


# time.sleep(4)


@then('User should be able to login to application')
def VerifyLogin(context):
    pass



@then('User should be on Homepage of the application.')
def VerifyHomepage(context):
    pass

@then('Logout the application')
def Logout(context):
    pass

@then('close browser')
def CloseBrowser(context):
    logger_login.info("browser closed")
    time.sleep(4)
    driver.close()
    driver.quit()