import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils

u = fun_utils

def run(**k):
    u.dfn()

    driver = k.get('driver')

    # driver.get('http://localhost:8000/')
    
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "emp_port_reg")))

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/admin_page/02a_employer_login.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "oiss_id_log_in")))
    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "userId")
    input_tag.send_keys("1")

    input_tag = form.find_element(By.NAME, "uPassword")
    input_tag.send_keys("demo")

    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()




    u.dfn()
