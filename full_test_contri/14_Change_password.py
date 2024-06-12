
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
  
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "change-password")))


    link=driver.find_element(By.CLASS_NAME,"change-password")
    print('link0',link)
    link.click()

    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    BE_DCTB_CONTRI_REG_SUBMISSION_NO = driver.execute_script('return window.localStorage.getItem("BE_DCTB_CONTRI_REG_SUBMISSION_NO");')

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "username")
    input_tag.send_keys(BE_DCTB_CONTRI_REG_SUBMISSION_NO)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(BE_DCTB_CONTRI_REG_SUBMISSION_NO)

    
    input_tag = form.find_element(By.NAME, "newpassword")
    input_tag.send_keys(BE_DCTB_CONTRI_REG_SUBMISSION_NO)


    btn = driver.find_element(By.ID, "oiss_id_reset")
    btn.click()
    u.dsleep(3)
    u.dfn()
 
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    BE_DCTB_CONTRI_REG_SUBMISSION_NO = driver.execute_script('return window.localStorage.getItem("BE_DCTB_CONTRI_REG_SUBMISSION_NO");')

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "username")
    input_tag.send_keys(BE_DCTB_CONTRI_REG_SUBMISSION_NO)


    input_tag = form.find_element(By.NAME, "password")
    input_tag.send_keys(BE_DCTB_CONTRI_REG_SUBMISSION_NO)

    btn = driver.find_element(By.ID, "oiss_id_log_in")
    btn.click()
    u.dsleep(3)

    
    

