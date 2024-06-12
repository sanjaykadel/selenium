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

    #print('kargs', k)
    driver = k.get('driver')
        
    curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_informal/cont_informal_reg_login.html'
    if driver.current_url != curl:
        
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_SUBMISSION")))
   
   
    informal_reg_submission_no = driver.execute_script('return window.localStorage.getItem("BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO");')
    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "submissionNo")
    input_tag.send_keys(informal_reg_submission_no)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(informal_reg_submission_no)

    input_tag = form.find_element(By.NAME, "uName")
    input_tag.send_keys(informal_reg_submission_no)

    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()

    u.dfn()
    u.env_pause()

