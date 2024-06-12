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
    curl=f'{u.getUrl()}/?_P_PAGE_=entity\components\BE_OISS_USERS_CUSTOM.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    informal_reg_submission_no =driver.execute_script('return window.localStorage.getItem("CONT_SELF_REG_SUBMISSION_NO");')


      

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "username")
    input_tag.send_keys(informal_reg_submission_no)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(informal_reg_submission_no)


    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wrapper")))


    # button = driver.find_element(By.TAG_NAME,"button")
    link=driver.find_element(By.ID,"password")
    print('link0',link)
    link.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    informal_reg_submission_no =driver.execute_script('return window.localStorage.getItem("CONT_SELF_REG_SUBMISSION_NO");')


      

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "username")
    input_tag.send_keys(informal_reg_submission_no)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(informal_reg_submission_no)

    input_tag = form.find_element(By.NAME, "newpassword")
    input_tag.send_keys(informal_reg_submission_no)



    btn = driver.find_element(By.ID, "oiss_id_reset")
    btn.click()


    # link = driver.find_element(By.CLASS_NAME, "")
    # link.click()
    # u.dsleep()

    
    # link = driver.find_element(By.CLASS_NAME, "main")
    # link1 =link.find_element(By.ID, "nav")
    # link2 =link1.find_element(By.CLASS_NAME, "nav-second-section")
    # link3 =link2.find_element(By.CLASS_NAME, "list-group-item")
    # BUTTON=link3.find_element(By.ID,"kyc")
    # BUTTON.click()

    u.dfn()
    u.env_pause()
    

