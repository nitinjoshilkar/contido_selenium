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
import pyautogui

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
logger_snppgm= logging.getLogger('scontido_snppgm_flow.py')
driver = webdriver.Chrome()

try:
	URL_PATH = config('URL')
	wait_time= 1
	#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver.implicitly_wait(1)
	driver.maximize_window()
	actions = ActionChains(driver)
	driver.get(URL_PATH)
	logger_snppgm.info("SNP executive user Connection created successfully")
	''' login '''
	username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
	username.clear()
	username.send_keys(config('snp_executive_user'))
	time.sleep(2)
	password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
	password.clear()
	password.send_keys(config('snp_executive_password'))
	time.sleep(2)
	''' close chat box '''
	pyautogui.moveTo(1345, 670,duration=1)
	pyautogui.click(1345, 670)
	pyautogui.moveTo(1325, 430,duration=1)
	pyautogui.click(1325, 430)              
	time.sleep(2)
	login= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
	login.click()
	#time.sleep(4)
	logger_snppgm.info("SNP executive user login successfully")
	time.sleep(4)
	''' player basic testing video '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Show']")))
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[1]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="5f3c116c95eabf1752721898"]').click()
	time.sleep(4)
	''' select source clean '''
	pyautogui.moveTo(220, 180)
	pyautogui.click(220, 180)
	time.sleep(2)
	pyautogui.moveTo(320, 380)
	pyautogui.click(320, 380)
	time.sleep(2)
	''' play pause button'''
	#play_pause_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/button[1]')
	#play_pause_button.click()
	#time.sleep(2)
	#pyautogui.moveTo(500, 531)
	#pyautogui.click(500, 531)
	#time.sleep(2)
	##play_pause_button.click()
	#time.sleep(3)
	#''' volume button '''
	#volume_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/div[4]/button')
	#volume_button.click()
	#time.sleep(3)
	#volume_button.click()
	#time.sleep(4)
	#logger_snppgm.info("Volume button working fine")
	#''' audio track testing'''
	#hdenable_disable= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/div[5]/button')
	#hdenable_disable.click()
	#time.sleep(2)
	#driver.find_element_by_xpath("//div[@class='AudioTracksMenuButton__AudioTrackBlock-sc-1q6zu8b-0 jxgKuv']")
	#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Trk 3 St M&E']"))).click()
	#time.sleep(3)
	#driver.find_element_by_xpath("//div[@class='AudioTracksMenuButton__AudioTrackBlock-sc-1q6zu8b-0 jxgKuv']")
	#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Trk 8 St SFX']"))).click()
	#time.sleep(3)
	#''' safe area testing '''
	##driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/div[6]/button').click()
	##time.sleep(1)
	##driver.find_element_by_xpath("//div[@class='SafeAreaControl__SafeAreaBlock-sc-1q5sjvv-0 hzWRGl']")
	##wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='4:3 Safe Area']"))).click()
	##time.sleep(2)
	##logger_snppgm.info("safe area test working fine")
	##time.sleep(5)
	#''' forward button '''
	#forwardreplay_button1= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/button[3]')
	#for replay in range(7):
	#	forwardreplay_button1.click()
	#	time.sleep(1)
	#logger_snppgm.info("forwardreplay button testing works fine")
	#time.sleep(4)
	#''' backward button '''
	#backwardplay_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[4]/div/button[2]')
	#for replay in range(5):
	#	backwardplay_button.click()
	#	time.sleep(1)
	#logger_snppgm.info("backwardreplay button testing works fine")
	#time.sleep(4)
	#''' segments '''
	#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Segments']"))).click()
	#time.sleep(3)
	#logger_snppgm.info("segments tab selected")
	##driver.find_element_by_xpath("//div[@class='segment-details']")
	##wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Ttielsf']"))).click()
	##time.sleep(5)
	##segment_back_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/button').click()
	##time.sleep(4)
	##driver.find_element_by_xpath("//div[@class='segment-details']")
	##wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='sdfasdf']"))).click()
	##time.sleep(5)
	##segment_back_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/button').click()
	##time.sleep(4)
	''' Clevr Tags '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Clevr Tags']"))).click()
	time.sleep(3)
	logger_snppgm.info("Clevr Tags selected")
	''' snp edit button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/button').click()	
	time.sleep(4)
	logger_snppgm.info('snp edit button click')
	#''' start pointer '''
	#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[4]/button[1]').click()
	#time.sleep(2)
	#play_pause_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/button[1]')
	#play_pause_button.click()
	#logger_snppgm.info('start pointer')
	#time.sleep(6)
	#''' end pointer '''
	#pyautogui.moveTo(320, 660)
	#pyautogui.click(320, 660)
	#time.sleep(1)
	#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[4]/button[2]').click()
	#time.sleep(2)
	#logger_snppgm.info('end pointer')
	#play_pause_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/button[1]')
	#play_pause_button.click()
	#''' comment button click '''
	#comment_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/button')
	#comment_button.click()
	#logger_snppgm.info("comment button clicked")
	#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div')
	#driver.find_element_by_xpath("//div[@class='AudioTracksMenuButton__AudioTrackBlock-sc-1q6zu8b-0 jxgKuv']")
	#wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Comment']"))).click()
	#comment = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div/div[1]/div/textarea')
	#comment.send_keys('selenium testing comment')
	#comment_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div/div[1]/button[2]')
	#comment_button.click()
	#logger_snppgm.info("comment add successfully")
	#time.sleep(3)
	#''' can not add new remark close button '''
	#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/button').click()
	#time.sleep(2)
	''' other review master visited '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]')
	''' Review Master 2 '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Review Master 2']"))).click()
	time.sleep(2)
	logger_snppgm.info('Review Master 2 is selected')
	''' start pointer '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[4]/button[1]').click()
	time.sleep(2)
	play_pause_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/button[1]')
	play_pause_button.click()
	logger_snppgm.info('start pointer')
	time.sleep(6)
	''' end pointer '''
	pyautogui.moveTo(320, 660)
	pyautogui.click(320, 660)
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[4]/button[2]').click()
	time.sleep(2)
	logger_snppgm.info('end pointer')
	play_pause_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/button[1]')
	play_pause_button.click()
	''' comment button click '''
	comment_button= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/button')
	comment_button.click()
	logger_snppgm.info("comment button clicked")
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div')
	driver.find_element_by_xpath("//div[@class='AudioTracksMenuButton__AudioTrackBlock-sc-1q6zu8b-0 jxgKuv']")
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Comment']"))).click()
	comment = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div/div[1]/div/textarea')
	comment.send_keys('selenium testing comment')
	comment_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div/div[1]/button[2]')
	#comment_button.click()
	logger_snppgm.info("comment add successfully")
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[3]/div/div[5]/div/div/div/div[1]/button[1]').click()
	logger_snppgm.info("comment close button clicked")
	''' submit for approval '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div[1]/button').click()
	time.sleep(2)
	logger_snppgm.info("submit for approval button clicked")
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/button[2]').click()
	logger_snppgm.info("submit review no button clicked")
	time.sleep(2)
	''' review master 3 selected '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]')
	''' Review Master 3 '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Review Master 3']"))).click()
	logger_snppgm.info("Review Master 3 is selected")
	time.sleep(3)
	''' snp_pgm close button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div[2]/button')
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Exit']"))).click()
	time.sleep(2)
	logger_snppgm.info("Exit button clicked")
	''' back button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/button').click()
	time.sleep(1)
	logger_snppgm.info("back button clicked")
	''' sign out '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]').click()
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]').click()
	#time.sleep(1)
	logger_snppgm.info("SNP executive user sign out successfully")
	''' close driver '''
	driver.close()
	driver.quit()
	time.sleep(4)
	''' login snp admin user '''
	URL_PATH = config('URL')
	wait_time= 1
	#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.maximize_window()
	actions = ActionChains(driver)
	driver.get(URL_PATH)
	logger_snppgm.info("SNP admin user Connection created successfully")
	username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
	username.clear()
	username.send_keys(config('snp_admin_user'))
	time.sleep(2)
	password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
	password.clear()
	password.send_keys(config('snp_admin_password'))
	time.sleep(2)
	''' close chat box '''
	pyautogui.moveTo(1345, 670)
	pyautogui.click(1345, 670)
	pyautogui.moveTo(1325, 430)
	pyautogui.click(1325, 430)              
	time.sleep(2)
	login= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
	login.click()
	time.sleep(4)
	logger_snppgm.info("snp admin user login successfully")
	''' video selected '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Show']")))
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[1]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[2]').click()
	time.sleep(2)
	#driver.find_element_by_xpath('//*[@id="5f35810d95eabf3c8d7680d9"]').click()
	driver.find_element_by_xpath('//*[@id="5f3c116c95eabf1752721898"]').click()
	time.sleep(4)
	''' select source clean '''
	pyautogui.moveTo(220, 180,duration=1)
	pyautogui.click(220, 180)
	time.sleep(2)
	pyautogui.moveTo(320, 380,duration=1)
	pyautogui.click(320, 380)
	time.sleep(2)
	''' snp edit button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/button').click()	
	time.sleep(4)
	logger_snppgm.info('snp edit button click')
	''' review master 3 selected '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]')
	''' Review Master 3 '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Review Master 3']"))).click()
	logger_snppgm.info("Review Master 3 is selected")
	time.sleep(3)
	''' Review Master 2 '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Review Master 2']"))).click()
	logger_snppgm.info("Review Master 2 is selected")
	''' proceed to approval '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div[1]/button').click()
	time.sleep(3)
	''' close button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/button[2]').click()
	time.sleep(3)
	''' exit button '''
	# //*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div[2]/button
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div[2]/button').click()
	time.sleep(1)
	logger_snppgm.info("close button clicked")
	''' back button '''
	# //*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/button
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/button').click()
	time.sleep(1)
	logger_snppgm.info("back button clicked")
	''' sign out '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]').click()
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]').click()
	#time.sleep(2)
	logger_snppgm.info("SNP admin user sign out successfully")
	''' close driver '''
	driver.close()
	driver.quit()
	time.sleep(4)
	''' login pgm executive user '''
	URL_PATH = config('URL')
	wait_time= 1
	#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.maximize_window()
	actions = ActionChains(driver)
	driver.get(URL_PATH)
	logger_snppgm.info("PGM executive user Connection created successfully")
	username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
	username.clear()
	username.send_keys(config('pgm_executive_user'))
	time.sleep(2)
	password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
	password.clear()
	password.send_keys(config('pgm_executive_password'))
	time.sleep(2)
	''' close chat box '''
	pyautogui.moveTo(1345, 670,duration=1)
	pyautogui.click(1345, 670)
	pyautogui.moveTo(1325, 430,duration=1)
	pyautogui.click(1325, 430)              
	time.sleep(2)
	login= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
	login.click()
	time.sleep(4)
	logger_snppgm.info("pgm executive user login successfully")
	''' video selected '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Show']")))
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[1]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[2]').click()
	time.sleep(2)
	#driver.find_element_by_xpath('//*[@id="5f35810d95eabf3c8d7680d9"]').click()
	driver.find_element_by_xpath('//*[@id="5f3c116c95eabf1752721898"]').click()
	time.sleep(4)
	''' select source clean '''
	pyautogui.moveTo(220, 180)
	pyautogui.click(220, 180)
	time.sleep(2)
	pyautogui.moveTo(320, 380)
	pyautogui.click(320, 380)
	time.sleep(2)
	#time.sleep(4)
	''' snp edit button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/button').click()	
	time.sleep(4)
	logger_snppgm.info('pgm edit button click')
	''' close button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div/button').click()
	time.sleep(1)
	logger_snppgm.info("close button clicked")
	''' back button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/button').click()
	time.sleep(1)
	logger_snppgm.info("back button clicked")
	''' sign out '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]').click()
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]').click()
	#time.sleep(2)
	logger_snppgm.info("PGM executive user sign out successfully")
	''' close driver '''
	driver.close()
	driver.quit()
	time.sleep(4)
	''' login pgm admin user '''
	URL_PATH = config('URL')
	wait_time= 1
	#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.maximize_window()
	actions = ActionChains(driver)
	driver.get(URL_PATH)
	logger_snppgm.info("PGM admin user Connection created successfully")
	#time.sleep(1)
	username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[1]/input')
	username.clear()
	username.send_keys(config('pgm_admin_user'))
	#time.sleep(2)
	password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/form/div[2]/input')
	password.clear()
	password.send_keys(config('pgm_admin_password'))
	#time.sleep(2)
	''' close chat box '''
	#pyautogui.moveTo(1345, 670,duration=2)
	#pyautogui.click(1345, 670)
	#pyautogui.moveTo(1325, 430,duration=2)
	#pyautogui.click(1325, 430)              
	#time.sleep(2)
	login= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/button')
	login.click()
	time.sleep(4)
	logger_snppgm.info("pgm admin user login successfully")
	''' video selected '''
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Show']")))
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[1]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[2]/div[2]').click()
	time.sleep(2)
	#driver.find_element_by_xpath('//*[@id="5f35810d95eabf3c8d7680d9"]').click()
	driver.find_element_by_xpath('//*[@id="5f3c116c95eabf1752721898"]').click()
	time.sleep(4)
	''' select source clean '''
	pyautogui.moveTo(220, 180)
	pyautogui.click(220, 180)
	time.sleep(2)
	pyautogui.moveTo(320, 380)
	pyautogui.click(320, 380)
	time.sleep(2)
	#time.sleep(4)
	''' snp edit button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/button').click()	
	time.sleep(4)
	logger_snppgm.info('pgm edit button click')
	''' close button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[3]/div[3]/div/div/button').click()
	time.sleep(1)
	logger_snppgm.info("close button clicked")
	''' back button '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/button').click()
	time.sleep(1)
	logger_snppgm.info("back button clicked")
	''' sign out '''
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]')
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]').click()
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]').click()
	#time.sleep(2)
	logger_snppgm.info("PGM admin user sign out successfully")
	time.sleep(2)
	## player tagging testing video
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Rushes']")))
	driver.find_element_by_xpath("//div[@id='5bf6580c40284365d82f2efb']").click()
	time.sleep(4)
	tagging_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[3]/div[2]/button')
	tagging_button.click()
	time.sleep(4)
	print('tagging_button click')
	asset_name= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/input')
	story_name= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/input')
	story_name.clear()
	story_name.send_keys('Sabarimala  court case')
	print('story name added')
	# <div class="sc-hIVACf lgIDJp"><div class="sc-jTzLTM kQPoo"><input type="number" label="DD" placeholder="DD" class="sc-jzJRlG kCZKhN" value="19"><label class="floaton">DD</label></div><div class="sc-jTzLTM kQPoo"><input type="number" label="MM" placeholder="MM" class="sc-jzJRlG kCZKhN" value="04"><label class="floaton">MM</label></div><div class="sc-jTzLTM kQPoo"><input type="number" label="YYYY" placeholder="YYYY" class="sc-jzJRlG kCZKhN" value="2019"><label class="floaton">YYYY</label></div></div>
	driver.find_element_by_xpath("//div[@class='sc-hIVACf lgIDJp']")
	driver.find_element_by_xpath("//div[@class='sc-jTzLTM kQPoo']")
	date= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div[1]/input')
	date.click()
	for date_data in range(2):
		date.send_keys(Keys.BACKSPACE)
	date.send_keys('27')
	time.sleep(1)
	#print('day')
	driver.find_element_by_xpath("//div[@class='sc-jTzLTM kQPoo']")
	month= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div[2]/input')
	month.click()
	for month_data in range(2):
		month.send_keys(Keys.BACKSPACE)
	month.send_keys('8')
	time.sleep(1)
	driver.find_element_by_xpath("//div[@class='sc-jTzLTM kQPoo']")
	year= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div[3]/input')
	year.click()
	for year_data in range(4):
		year.send_keys(Keys.BACKSPACE)
	year.send_keys('2018')
	time.sleep(1)
	regional_asset_name= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/input')
	regional_asset_name.clear()
	regional_asset_name.send_keys('వైజ్ఞానిక శాస్త్రాంశాల ఆధారంగా సృ')
	time.sleep(3)
	genre= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[5]/div/button')
	genre.click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='accidents']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='agriculture']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='awards']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='education']"))).click()
	genre_update_button= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/button[1]')
	genre_update_button.click()
	time.sleep(1)
	print('genre updated')
	personality= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[6]/div/button')
	personality.click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='achiever']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='athlete']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='film star']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='musician']"))).click()
	personality_update_button= driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/button[1]')
	personality_update_button.click()
	print('personality updated')
	time.sleep(2)
	##visuals	
	visuals= driver.find_element_by_xpath('//*[@id="visuals"]/div/input')
	visuals.send_keys('sandy')
	time.sleep(3)
	visuals.send_keys(Keys.ENTER)
	visual_data=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[7]/div/div[2]/p')
	time.sleep(2)
	visual_data.click()
	##mentions
	mentions= driver.find_element_by_xpath('//*[@id="mentions"]/div/input')
	mentions.send_keys('galaxy')
	time.sleep(3)
	mentions.send_keys(Keys.ENTER)
	mentions_data=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/p')
	time.sleep(2)
	mentions_data.click()
	##keywords
	keywords= driver.find_element_by_xpath('//*[@id="keywords"]/div/input')
	keywords.send_keys('note')
	time.sleep(3)
	keywords.send_keys(Keys.ENTER)
	keywords_data=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/div[2]/p')
	time.sleep(2)
	keywords_data.click()
	# <div class="sc-kQsIoO jlBCqN searchable-section"><p class="dropdown-label">Content format</p><span class="sc-htoDjs jYjAhm sc-gPzReC fcWAIn"> protest <a class="sc-iwsKbI nMAWW sc-gPzReC fcWAIn"><span>X</span></a> </span><input type="text" class="sc-cpmKsF jxdiWb" value=""></div>
	#content format
	driver.find_element_by_xpath("//div[@class='sc-kQsIoO jlBCqN searchable-section']")
	content_format= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[10]/div/button')
	content_format.click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='rally']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='protest']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='ugc']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='others']"))).click()
	content_format_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/button[1]')
	content_format_button.click()
	#category
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='generic']"))).click()
	#relevance
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='international']"))).click()
	#content rating
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='popular']"))).click()
	#sentiments
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='neutral']"))).click()
	#political parties
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='cpm']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='cpi']"))).click()
	driver.find_element_by_xpath("//div[@class='sc-jAaTju fFmXJU']")
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='ani']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='news hq']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='slot']"))).click()
	wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='social media']"))).click()
	#synopsis
	driver.execute_script("window.scrollTo(2100,2500);")
	synopsis_text= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[17]/div/textarea')
	synopsis_text.clear()
	synopsis_text.send_keys('The longer he lived, the more bile he was becoming and the more')
	synopsis_text.send_keys('poisonous were his words. People avoided him, because his misfortune')
	time.sleep(2)
	#technical metadata
	reporter= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/input')
	reporter.clear()
	reporter.send_keys('Kriver Perter')
	narrator= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/input')
	narrator.clear()
	narrator.send_keys('Sunirtra Peoto')
	cameraman= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/input')
	cameraman.clear()
	cameraman.send_keys('Lato Laril')
	burea_location= driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[5]/div/input')
	burea_location.clear()
	burea_location.send_keys('Delhi')
	story_location= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[6]/div/input')
	story_location.clear()
	story_location.send_keys('hari hamani')
	time.sleep(4)
	save_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[3]/div/button[1]')
	save_button.click()
	time.sleep(3)
	# /html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[1]/div[1]/button
	back_button= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div[1]/div[1]/button')
	back_button.click()
	time.sleep(8)
	## player tagging testing video
	wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Latest Ingested: Rushes']")))
	driver.find_element_by_xpath("//div[@id='5bf6580c40284365d82f2efb']").click()
	time.sleep(8)
	driver.close()
	driver.quit()

except Exception as e:
	logger_snppgm.error('error in snp_pgm flow:{}'.format(e))
	driver.close()
	driver.quit()