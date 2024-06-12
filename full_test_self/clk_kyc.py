import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils

click_create=0
def run(**k):
    u.dfn()

    # print('kargs', k)
    driver = k.get('driver')
   
   
    u.frun(driver, 'full_test_self.kyc_click.kyc_button_click_profile')
    u.frun(driver, 'full_test_self.kyc_click.kyc_button_click_workdetail')
    u.frun(driver, 'full_test_self.kyc_click.kyc_button_click_address')
    u.frun(driver, 'full_test_self.kyc_click.kyc_button_click_document')
    u.frun(driver, 'full_test_self.kyc_click.kyc_button_click_relative')
    
    

    return
