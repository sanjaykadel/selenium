

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

    ######### Employer  
   
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_EMPLOYER")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    
    ######## Address

    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    
    
    u.dfn()

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
   
    u.dsleep(3)


    ########### Contact 

    tab=driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()
    
    u.dfn()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_CONTACT")
    
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    
    
    u.dfn()

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)

    ########## doc

    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
       
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    u.dsleep(2)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    ############### Executive Head 

    tab=driver.find_element(By.ID, "id_oiss_tab_executive_head")
    tab.click()

   
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    u.dsleep(2)
    u.dfn()
    
    ########### Chairman 
    driver.execute_script("window.scrollBy(0, -200);")
    u.dsleep(2)
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_chairman")
    tab.click()
    u.dfn()
    form = driver.find_element(
        By.ID, "id_oiss_tab_content_chairman_head")
    
    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)

    u.dfn()
    ############# Contact person 
    driver.execute_script("window.scrollBy(0, -200);")
    u.dsleep(2)
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contact_person")
    tab.click()

    form = driver.find_element(By.ID, "id_oiss_tab_content_contact_person_head")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollBy(0, -300);")

    u.dsleep(3)

    u.dfn()








   

   
    
    
    
  

    

    
   
    
