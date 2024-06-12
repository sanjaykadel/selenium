

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
   

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
  
    # driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_PERSON")
    

   

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    
   
   

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")

    u.dfn()
    
    # el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    # el.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")
    table = form.find_element(By.CLASS_NAME, "table-responsive")

    u.dfn()

    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
   
    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    # el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    # el.send_keys(Keys.ENTER)
    # u.dfn()
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_doc")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_DOC")

    # el = form.find_element(By.NAME, "docId")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = form.find_element(By.NAME, "issueNo")
    # el.send_keys("111111")

    # el = u.ufind_element(driver,form,By.NAME, "issueDate")
    # el.send_keys("2007-09-08")
    # u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")


    # el = form.find_element(By.NAME, "issuePlace")
    # el.send_keys("Sanepa")


    # el = u.ufind_element(driver,form,By.NAME, "issueDate")
    # el.send_keys("2007-09-08")
    # u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")


    # el = u.ufind_element(driver,form,By.NAME, "issuePlace")
    # el.send_keys("Sanepa")

    # el = form.find_element(By.NAME, "docfile")
    # el.send_keys(u.sampleFile('tiny.pdf'))
    
    # el = form.find_element(By.NAME, "docbackfile")
    # el.send_keys(u.sampleFile('tiny.pdf'))

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()


    
    WebDriverWait(driver, 500).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_relative_so")))


    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_content_person_relative_so")     
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver,form,By.NAME, "relId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
    el = u.ufind_element(driver, form, By.NAME, "fnameNep")
    el.send_keys("राम")

    el = u.ufind_element(driver, form, By.NAME, "mnameNep")
    el.send_keys("बहादुर")

    el = u.ufind_element(driver, form, By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form, By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form, By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form, By.NAME, "lnameEng")
    el.send_keys("Thapa")

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-05")

    el = u.ufind_element(driver, form, By.NAME, "gender")
    el.send_keys("male")

    
    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.env_pause()

   
    
    
  

   

    

   
    
   
    
    
   
    

   

   
    
    
    
  

    

    
   
    
