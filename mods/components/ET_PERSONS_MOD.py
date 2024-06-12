import os
# os.system('cls')

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

    curl = f'{u.getUrl()}/?_P_PAGE_=mods/components/ET_PERSONS/ET_PERSONS_MOD.html'
 
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "class_oiss_gen_content_ET_PERSONS")))

    ######  ET_PERSON ############

    u.dfn()
    form = k.get('form')
    if not form:
        form = driver.find_element(

            By.CLASS_NAME, "class_oiss_gen_form_ET_PERSONS")

    el = u.ufind_element(driver, form, By.NAME, "eid")
    el.send_keys("4")

    el = u.ufind_element(driver, form, By.NAME, "submissionNo")
    el.send_keys("4")
 
    el = u.ufind_element(driver, form, By.NAME, "fnameNep")
    el.send_keys("राम")


    el = u.ufind_element(driver, form, By.NAME, "mnameNep")
    el.send_keys("बहादुर")
    
    el = u.ufind_element(driver, form, By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form, By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form, By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form, By.NAME, "lnameEng")
    el.send_keys("Thapa")
    
    el = u.ufind_element(driver, form, By.NAME, "grandFatherName")
    el.send_keys("Hari")

    el = u.ufind_element(driver, form, By.NAME, "fatherName")
    el.send_keys("umesh")

    el = form.find_element(By.NAME, "altCountry")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

    el = form.find_element(By.NAME, "altRelType")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    
    el = form.find_element(By.NAME, "altGender")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)
   
    el = form.find_element(By.NAME, "altBloodGroup")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
