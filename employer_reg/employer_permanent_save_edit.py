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
        
    curl='http://localhost:8000/?_P_PAGE_=pages/kyc_page/02_employer_edit_profile.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "id_oiss_tab_employer")))

    ################# BE_CTB_EMPLOYER_KYC #################

    tab = driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()

    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_CTB_EMPLOYER_KYC")

    # emp_reg_submission_no = driver.execute_script('return window.localStorage.getItem("EMP_REG_SUBMISSSION_NO");')

    # el = form.find_element(By.NAME, "username")
    # el.send_keys(int(emp_reg_submission_no))

    # el = form.find_element(By.NAME, "password")
    # el.send_keys(int(emp_reg_submission_no))

    # btn = driver.find_element(By.ID, "oiss_id_log_in")
    # btn.click()

    ################# BE_CTB_ADDRESS_KYC #################

    tab = driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()
    ################# BE_CTB_PERSON_KYC #################

    tab = driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()
    ################# BE_CTB_EMP_DOC_KYC #################

    tab = driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()
    ################# BE_ZQUERY #################

    tab = driver.find_element(By.ID, "id_oiss_tab_query")
    tab.click()




    u.dfn()
