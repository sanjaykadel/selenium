import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()

    driver = k.get('driver')
    frun=k.get('frun')

  

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    
    u.frun(driver, 'kyc_click.kyc_button_click_profile')
    u.frun(driver, 'kyc_click.kyc_button_click_workdetail')
    u.frun(driver, 'kyc_click.kyc_button_click_address')
    u.frun(driver, 'kyc_click.kyc_button_click_document')
    u.frun(driver, 'kyc_click.kyc_button_click_relative')
    
    

    return
