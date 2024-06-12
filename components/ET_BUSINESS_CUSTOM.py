import os
#os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import fun_utils
u = fun_utils


def run(**k):
    #print('kargs', k)
    u.dfn()

    driver = k.get('driver')
    driver.get('http://localhost:8000/?_P_PAGE_=ET_BUSINESS/ET_BUSINESS.html')
    
    
 
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_BUSINESS")))


    ###### ET_BUSINESS ########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_BUSINESS")

    el = form.find_element(By.NAME, "companyName")
    el.send_keys("Tinker")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("kathmandu")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9825998443")
    
    el = form.find_element(By.NAME, "contributionAmount")
    el.send_keys("1000")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
