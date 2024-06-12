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
    u.dfn()

    driver = k.get('driver')
    curl = 'http://127.0.0.1:8000/?_P_PAGE_=entity\components\ET_EMPLOYER_CUSTOM.html'
    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)
    
    
    
 
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_EMPLOYER")))


    ###### ET_EMPLOYER #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_EMPLOYER")

    el = form.find_element(By.NAME, "employerNameNep")
    el.send_keys("Bromish")

    el = form.find_element(By.NAME, "employerNameEng")
    el.send_keys("Bromish")


    el = form.find_element(By.NAME, "etypeId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "stypeId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "indZoneCatId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "calendar")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "alertSource")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)
    
    el = form.find_element(By.NAME, "alertSourceVal")
    el.send_keys("bromishbista2003@gmail.com")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()

    u.env_pause()