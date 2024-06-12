

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

    WebDriverWait(driver, 500).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_relative_so")))


    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_content_person_relative_so")     
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver,form,By.NAME, "relId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
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

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-05")

    el = u.ufind_element(driver, form, By.NAME, "gender")
    el.send_keys("male")

    
    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.env_pause()

   
    