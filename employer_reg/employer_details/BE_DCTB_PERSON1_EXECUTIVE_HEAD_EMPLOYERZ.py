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

    curl = 'http://localhost:8000/?_P_PAGE_=pages/03_employer_entry_details1.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "id_oiss_tab_employer")))

    tab = driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_PERSON1_EXECUTIVE_HEAD_EMPLOYERZ")

    ####### BE_DCTB_PERSON1_EXECUTIVE_HEAD_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_executive_head")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON1_EXECUTIVE_HEAD_EMPLOYERZ")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("निमेश")

    
    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("निमेश")

        
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("कार्की")

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
        
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("98415222422")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
