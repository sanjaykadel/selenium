
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
    curl = f'{u.getUrl()}/?_P_PAGE_=entity\components\ET_WORKAREA_CUSTOM.html'
    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_WORKAREA")))
    
 
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_WORKAREA")
    
    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.NAME, "companyName")
    el.send_keys("Tinker")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("Kathmandu")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9876542312")

    el = form.find_element(By.NAME, "post")
    el.send_keys("intern")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()

    