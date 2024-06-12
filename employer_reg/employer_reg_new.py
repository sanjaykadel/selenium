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

    curl='http://localhost:8000/?_P_PAGE_=pages/01_employer_signup.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    #oiss_gen_form oiss_gen_form_BE_DCTB_SUBMISSION_EMPSIGNUPZ
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "oiss_class_sign_up")))
    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "userId")
    input_tag.send_keys("demo")

    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys("demo")

    input_tag = form.find_element(By.NAME, "uName")
    input_tag.send_keys("demo")

    input_tag = form.find_element(By.NAME, "phoneNo")
    input_tag.send_keys("demo")

    input_tag = form.find_element(By.NAME, "address")
    input_tag.send_keys("demo")

    input_tag = form.find_element(By.NAME, "email")
    input_tag.send_keys("demo")


    btn = driver.find_element(By.ID, "oiss_class_sign_up")
    btn.click()

    u.dfn()

