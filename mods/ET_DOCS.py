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
    
    curl = '127.0.0.1:8000/?_P_PAGE_=mods/components/ET_DOC/ET_DOCS_MOD.html'
    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_ET_DOCS")))
    
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_DOCS")
    
    
    el = u.ufind_element(driver, form,By.NAME, "altDocType")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("546789")

    el = form.find_element(By.NAME, "issueDate")
    el.send_keys("2080.09.09")

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))


    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    u.dfn()
    