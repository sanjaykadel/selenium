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

    curl='http://localhost:8000/?_P_PAGE_=pages/02_employer_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_SUBMISSIONZ_EMPLOYER_LOGINZ")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_SUBMISSIONZ_EMPLOYER_LOGINZ")

    u.dfn()

    emp_reg_submission_no = driver.execute_script('return window.localStorage.getItem("EMP_REG_SUBMISSSION_NO");')

    input_tag = form.find_element(By.NAME, "submissionNo")
    input_tag.send_keys(int(emp_reg_submission_no))


    input_tag = form.find_element(By.NAME, "uName")
    input_tag.send_keys(int(emp_reg_submission_no))

    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(int(emp_reg_submission_no))

    btn = driver.find_element(By.ID, "oiss_class_log_in")
    btn.click()

    u.dfn()


# below should fail because str in submission no
def run111111111111111111111(**k):
    u.dfn()

    driver = k.get('driver')

    curl='http://localhost:8000/?_P_PAGE_=pages/02_employer_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "oiss_class_log_in")))
    emp_reg_submission_no = driver.execute_script('return window.localStorage.getItem("EMP_REG_SUBMISSION_NO");')
    
    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "submissionNo")
    input_tag.send_keys(emp_reg_submission_no)


    input_tag = form.find_element(By.NAME, "uName")
    input_tag.send_keys(emp_reg_submission_no)

    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(emp_reg_submission_no)

    btn = driver.find_element(By.ID, "oiss_class_log_in")
    btn.click()

    u.dfn()
