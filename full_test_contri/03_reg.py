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
    curl = f'{u.getUrl()}/'
    

    # #####Clear the localstorage

     
     
   

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_profile")
    tab.click()
    
  
     ##### PERSON
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.ET_PERSON_CUSTOM',)
    u.dsleep(3) 
    
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_address")
    tab.click()
    # u.dsleep(3) 

    
    ###### ADDRESS
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.ET_ADDRESS1',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS") )
    u.dsleep(3) 

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Doc")
    tab.click()
    
   
    #### DOCUMENT
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.Document',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC") )
    u.dsleep(3) 
    
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Relative")
    tab.click()
  
    ##### Relative
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.Relative',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
    
    u.dsleep(3) 
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Bank")
    tab.click()

     
    ##### Bank
    u.fruns(driver=driver, lib='components.ET_BANK_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_BANK") )

    u.dsleep(3) 
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Employment")
    tab.click()

     
   ### Employment
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.ET_EMPLOYMENT',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_CTB_CONTRIBUTOR") )
   
   