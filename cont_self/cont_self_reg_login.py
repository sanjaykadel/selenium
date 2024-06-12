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

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/4so_contributor_sorojgar_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person_login_so")))
    so_reg_submission_no = driver.execute_script(
        'return window.localStorage.getItem("BE_DCTB_SO_REG_SUBMISSION_NO");')

    ####### BE_DCTB_PERSON_SO #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_LOGIN_SO")

    el = form.find_element(By.NAME, "submissionNo")
    el.send_keys(so_reg_submission_no)

    el = form.find_element(By.NAME, "dob")
    el.send_keys("2050.09.09")

    btn = driver.find_element(By.CLASS_NAME, "class_oiss_person_login_so")
    btn.send_keys(Keys.ENTER)
    # btn.click()
    u.dfn()
