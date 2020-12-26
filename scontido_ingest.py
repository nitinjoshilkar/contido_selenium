from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import os
#import pyatspi
import requests
import json
import time
import pyautogui
from decouple import config
import logging

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
logger_ingest= logging.getLogger('scontido_ingest.py')
driver = webdriver.Chrome()

try:
	URL_PATH = config('URL')
	wait_time= 1
	#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver.implicitly_wait(1)
	driver.maximize_window()
	actions = ActionChains(driver)
	driver.get(URL_PATH)
	logger_ingest.info("Connection created successfully")
	''' login '''
	username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
	username.clear()
	username.send_keys(config('operation_user'))
	time.sleep(2)
	password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
	password.clear()
	password.send_keys(config('operation_password'))
	time.sleep(2)
	''' close chat box '''
	pyautogui.moveTo(1345, 670,duration=2)
	pyautogui.click(1345, 670)
	pyautogui.moveTo(1325, 430,duration=2)
	pyautogui.click(1325, 430)
	time.sleep(2)
	login= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
	login.click()
	time.sleep(4)
	logger_ingest.info("login successfully")
	''' select connect '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Connect']"))).click()
	logger_ingest.info("'connect button click'")
	showname= driver.find_element_by_xpath('//*[@id="program_db_id"]/div/input')
	showname.clear()
	showname.send_keys('IPL league')
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="program_db_id"]/div[2]')
	pyautogui.moveTo(850, 510)
	time.sleep(2)
	pyautogui.click(850, 510)
	time.sleep(2)
	''' program info '''
	driver.find_element_by_xpath('//*[@id="season_no"]').click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='1']"))).click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="episode_no"]').click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='5']"))).click()
	episode_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/input')
	episode_name.send_keys('Nazar ka effect')
	''' calendar selected '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]').click()
	logger_ingest.info('program due date clicked')
	time.sleep(wait_time)
	month_header= driver.find_element_by_xpath("//div[@class='month-header']")
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='October']"))).click()
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='2020']"))).click()
	logger_ingest.info('month header selected')
	week_header= driver.find_element_by_xpath("//div[@class='week-header']")
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Fri']"))).click()
	logger_ingest.info('week header selected')
	weeks= driver.find_element_by_xpath("//div[@class='weeks']")
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='9']"))).click()
	logger_ingest.info('weeks selected')
	time.sleep(2)
	''' channel selected '''
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Asianet']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Maa HD']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='FC']"))).click()
	total_segments = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[6]/div/div/div/div/input')
	total_segments.clear()
	total_segments.send_keys('1')
	time.sleep(2)
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
	''' File info '''
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Tx Master']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Clean']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='India Tx']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='HD']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ingest']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Subtitle']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add Track']"))).click()
	time.sleep(1)
	logger_ingest.info('add track clicked')
	''' audio track mapping '''
	driver.find_element_by_xpath("//div[@class='sc-bsbRJL iolmbl']")
	track_no= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/div[1]')
	track_no.click()
	time.sleep(1)
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='01']"))).click()
	driver.find_element_by_xpath("//div[@class='sc-bsbRJL iolmbl']")
	category= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div/div[1]')
	category.click()
	time.sleep(1)
	wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Language track']"))).click()
	driver.find_element_by_xpath("//div[@class='sc-bsbRJL iolmbl']")
	audio_type= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div/div[2]/table/tbody/tr/td[3]/div/div/div[1]')
	audio_type.click()
	time.sleep(1)
	wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Mono']"))).click()
	driver.find_element_by_xpath("//div[@class='sc-bsbRJL iolmbl']")
	channel_layout= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/div[1]')
	channel_layout.click()
	time.sleep(1)
	wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Front: L']"))).click()
	driver.find_element_by_xpath("//div[@class='sc-bsbRJL iolmbl']")
	language= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div/div[2]/table/tbody/tr/td[5]/div/div/div[1]')
	language.click()
	time.sleep(1)
	wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='English']"))).click()
	wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
	''' upload info '''
	note = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/div/textarea')
	note.clear()
	note.send_keys('week in week keek is keek')
	fileupload=wait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Ingest']"))).click()
	logger_ingest.info('Web ingest button clicked')
	time.sleep(4)
	#pyautogui.moveTo(100, 150, duration = 5)
	#pyautogui.click(100, 150)
	#print(pyautogui.position())
	##pyautogui.click(800,20)
	##print(pyautogui.position())
	#print('window close')
	##print(type(fileupload))
	#print(os.getcwd())
	#fileupload.click()
	#filepath=fileupload.click(os.getcwd()+"/KPMAA_397--20171003081234752--PG--2012.mxf")
	#print(filepath)
	#time.sleep(10)
	#fileselected=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div/div/div/input")
	#fileselected.clear()
	#fileselected.send_keys(os.getcwd()+"/KPMAA_397--20171003081234752--PG--2012.mxf")
	#print('file selected successfully')
	##os.chdir()
	#time.sleep(30)
	driver.close()
	driver.quit()

except Exception as e:
	print('Failed to connect internet:{}'.format(e))
	driver.close()
	driver.quit()