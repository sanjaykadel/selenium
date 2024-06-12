

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

    ######### Person  
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
   
    ######## Address
    u.dsleep(2)

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_address")
    tab.click()
    u.dsleep(2)

   
    form = driver.find_element(By.CLASS_NAME, "table-responsive")
   
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    u.dsleep(3)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    
    u.dsleep(2)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
   
    # u.dfn()
    u.dsleep(3)
    ########## doc

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Doc")
    tab.click()
    u.dsleep(3)
    
    # u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.Document',
    #     form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC") )
    u.dsleep(3) 
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_DOC")


    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
   


    
    ########## Relative

    u.dfn()
    u.dsleep(1)
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Relative")
    tab.click()
   
    
    u.dfn()
      
    
    form = driver.find_element(
        By.ID, "id_oiss_content_contri_Relative")
    

       

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    
  
    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.dfn()



    ############### Bank

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Bank")
    tab.click()

   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_BANK")))


   
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_BANK")
    

    

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    
    u.dsleep(3)

   

    u.dfn()
   








   

   
    
    
    
  

    

    
   
    
