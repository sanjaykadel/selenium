import os

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
        
    curl = f'{u.getUrl()}/'
    if driver.current_url != curl:
           u.err('driver.current_url != curl')
    
    driver.get(curl)
   

    link = driver.find_element(By.CLASS_NAME, "employer_reg")
    link.click()
    u.dsleep()


    link = driver.find_element(By.CLASS_NAME, "remployer_reg_login")
    link.click()
    u.dsleep()

    u.dfn()
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_SUBMISSION")))
    emp_reg_submission_no = driver.execute_script('return window.localStorage.getItem("EMP_REG_SUBMISSSION_NO");')

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "submissionNo")
    input_tag.send_keys(emp_reg_submission_no)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(emp_reg_submission_no)

    input_tag = form.find_element(By.NAME, "uName")
    input_tag.send_keys(emp_reg_submission_no)

    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()

    u.dfn()

