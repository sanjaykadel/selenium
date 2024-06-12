SCHEME_ACCIDENT='Accident Scheme'
SCHEME_CRITICAL='Critical Illness Scheme'
myscheme=SCHEME_ACCIDENT

CHFID_CRITICAL_TEST='20760000077'
CHFID_NORMAL_TEST='20760000001'
mychfid=CHFID_NORMAL_TEST

if myscheme==SCHEME_CRITICAL:
	mychfid=CHFID_CRITICAL_TEST


import os
os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dprint(args,args1=None):
	print('*************************', args)

def step1():
	driver.get('http://172.16.20.123:3000/claim/healthFacilities')
	WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,  "//label[text()='Claim Administrator']")))

	#driver.get('http://172.16.20.123:3000/claim/healthFacilities')
	x = driver.find_element(By.XPATH,  "//label[text()='Claim Administrator']")
	#print(x)
	print(x.text)
	#print(dir(x))
	#print(x._parent)
	#print(x._parent.text)


	x = driver.find_element(By.XPATH,  "//label[text()='Claim Administrator']/parent::*")
	#print(x)
	print(x.text)
	input_tag = x.find_element(By.TAG_NAME,"input")
	print(input_tag)
	input_tag.send_keys("demo")
	# input_tag.send_keys("e")
	# input_tag.send_keys("m")
	# input_tag.send_keys("o")

	#WebDriverWait(driver, 4000)
	#https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html
	#print(dir(Keys))
	WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,  "//span[text()='1234 Demo Claim Admin']")))
	input_tag.send_keys(Keys.ARROW_DOWN)
	input_tag.send_keys(Keys.ENTER)

	dprint('step1 done')







def step2():
	x = driver.find_element(By.XPATH,  "//label[text()='Scheme']/parent::*")
	x = driver.find_element(By.XPATH,  "//div[text()='Select']")
	x.click()
	#input_tag = x.find_element(By.TAG_NAME,"input")
	#print(input_tag)
	#input_tag.click()
	#x.send_keys(Keys.ARROW_DOWN)
	#x.send_keys(Keys.ARROW_DOWN)
	#x.send_keys(Keys.ARROW_DOWN)
	#
	#x.send_keys(Keys.ENTER)

	li = driver.find_element(By.XPATH, f"//li[text()='{myscheme}']")
	li.click()

	dprint('step2 done')


def step3_mainbutton_submit_click():
	#x= driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiFab-root MuiFab-primary']")
	x= driver.find_element(By.XPATH,"//button[contains(@class,'MuiButtonBase-root') and contains(@class,'MuiFab-root') and contains(@class,'MuiFab-primary')]")
	x.click()
	dprint('step3 done')

def step4_crischemepage():
	step1()
	step2()
	step3_mainbutton_submit_click()
	dprint('step4 done')


def step5():
	x = driver.find_element(By.XPATH,  "//label[text()='SSFID']/parent::*")
	inputs = x.find_element(By.TAG_NAME,"input")
	inputs.send_keys(mychfid)
	dprint('step5 done')

def step6_claim_entry_subscheme():
	if myscheme==SCHEME_ACCIDENT:
		dprint('step6 done')
		return
	while(1):
		try:
			x = driver.find_element(By.XPATH,  "//label[text()='Scheme']/parent::*")
			x = x.find_element(By.XPATH,  "//div[@role='button']")
			x.click()
			#import pdb; pdb.set_trace();

			li = driver.find_element(By.XPATH, "//li[text()='Pre-diagnosis expenses']")
			if (li.text=='Pre-diagnosis expenses'):
				li.click()
				break	
		except Exception as e:
			print(e)	
	dprint('step6 done')

def step7_claim_entry_main_diagnosis(): # typying main diagnosis thingy
	if myscheme==SCHEME_CRITICAL:
		x = driver.find_element(By.XPATH,  "//label[text()='Crit Diagnosis']/parent::*")
	else:
		x = driver.find_element(By.XPATH,  "//label[text()='Main Diagnosis']/parent::*")
	input_tag = x.find_element(By.TAG_NAME,"input")
	input_tag.send_keys("Cholera")
	WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,  "//span[text()='A00 A00 Cholera ']")))
	input_tag.send_keys(Keys.ARROW_DOWN)
	input_tag.send_keys(Keys.ENTER)
	dprint('step7 done')

def step7_5_select_accident_employer():
	if myscheme != SCHEME_ACCIDENT:
		dprint('step7_5 ret done')
		return
	x = driver.find_element(By.XPATH,  "//label[text()='Employer']/parent::*")
	input_tag = x.find_element(By.TAG_NAME,"input")
	input_tag.send_keys('cdm')
	WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,  "//span[text()='CDM International Inc.']")))
	input_tag.send_keys(Keys.ARROW_DOWN)
	input_tag.send_keys(Keys.ENTER)
	dprint('step7_5 done')


def step8_claim_entry_service_item():
	service_value='OPD01 OPD'
	service_value='ADJS01 Adjustment Service'

	
	import time;
	input_tags=[]
	while(True):
		x = driver.find_element(By.XPATH,  "//span[text()='Service']/ancestor::table") # table ... th ... div .. span.text=Service
		input_tags = x.find_elements(By.TAG_NAME,"input")
		if not	input_tags:
			time.sleep(1)
			continue
		i0=input_tags[0]
		#input_tags[1].clear();input_tags[2].clear();input_tags[3].clear() # react state bind so not cleared bythis

		value=i0.get_property('value')
		#import pdb; pdb.set_trace();
		time.sleep(1)
		if(value == service_value):
			break
		i0.clear()

		i0.send_keys(service_value)
		i0.send_keys(Keys.ARROW_DOWN)
		i0.send_keys(Keys.ENTER)

	dprint('step8 setting services item')
	srvval="2"
	for i in range(1,4):
		ic=input_tags[i]
		icval=ic.get_property('value')
		if icval != srvval:
			ic.clear()
			ic.send_keys(srvval)

	dprint('step8 done')


def step9_fullstep_hf_to_critical_enter():
	#step7_5_select_accident_employer();return;
	#step8_claim_entry_service_item();return #check single steps example, before this

	step4_crischemepage()
	step5()
	step6_claim_entry_subscheme()
	step7_claim_entry_main_diagnosis()
	step7_5_select_accident_employer();
	step8_claim_entry_service_item()#;return
	#step3_mainbutton_submit_click()
	dprint('step9 done')

#step8_claim_entry_service_item()
step9_fullstep_hf_to_critical_enter()

#step4_crischemepage();
dprint('finished')