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

    curl = f'{u.getUrl()}?_P_PAGE_=entity\components\ET_GRIVENCE_CUSTOM.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_GRIVENCE")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_GRIVENCE") 
   
    el = u.ufind_element(driver, form, By.NAME, "employerId")
    el.send_keys("41")
   
    el = u.ufind_element(driver, form, By.NAME, "name")
    el.send_keys("sanjay")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2050-04-03")

    el = u.ufind_element(driver, form, By.NAME, "gender")
    el.send_keys("M")
       
    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9876543210")
       
    el = u.ufind_element(driver, form, By.NAME, "email")
    el.send_keys("sanjay@sanjay.gmail.com")
    
    el = u.ufind_element(driver, form, By.NAME, "grievanceStatement")
    el.send_keys("i didn't get any alert after i fill form 1week ago")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)