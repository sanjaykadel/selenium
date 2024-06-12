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

    curl='http://localhost:8000/?_P_PAGE_=pages/admin_page/02a_employer_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_SEC_EMP_CONT_LOGINZ")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_SEC_EMP_CONT_LOGINZ")

    input_tag = form.find_element(By.NAME, "userId")
    input_tag.send_keys(1)

    input_tag = form.find_element(By.NAME, "uPassword")
    input_tag.send_keys(1)

    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()

    u.dfn()

