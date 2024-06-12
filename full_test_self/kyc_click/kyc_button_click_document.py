

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
  

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_doc")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_DOC")


    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()
