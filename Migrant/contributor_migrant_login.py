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

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/012_contributor_migrant_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person_login_migrant")))
    migrant_reg_submission_no = driver.execute_script(
        'return window.localStorage.getItem("BE_DCTB_MIGRANT_REG_SUBMISSION_NO");')

    ####### BE_DCTB_PERSON_MIGRANT #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_LOGIN_MIGRANT")

    el = form.find_element(By.NAME, "submissionNo")
    el.send_keys(migrant_reg_submission_no)

    el = form.find_element(By.NAME, "dob")
    el.send_keys("2050.09.09")

    btn = driver.find_element(By.CLASS_NAME, "class_oiss_person_login_migrant")
    btn.send_keys(Keys.ENTER)
    # btn.click()
    u.dfn()