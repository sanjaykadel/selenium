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
    frun=k.get('frun')

    curl = 'http://localhost:8000/?_P_PAGE_=entity/employer/Employer_Entry_Details.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    tab=driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()

  
   
   
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_EMPLOYER")))
    
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_ADDRESS")))
   
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_CONTACT")))
    
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_DOC")))
    
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    

    
  
     ###### EMPLOYER
    # u.fruns(driver=driver, lib='components.ET_EMPLOYER_CUSTOM',
    #     form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_EMPLOYER") )
    
    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()
    

    ###### ADDRESS
    u.fruns(driver=driver, lib='components.ET_ADDRESS_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS") )
    
    tab=driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()


    ##### CONTACT
    u.fruns(driver=driver, lib='components.ET_CONTACT_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_CONTACT") )
    
    
    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()

    
    #### DOCUMENT
    u.fruns(driver=driver, lib='components.ET_DOC_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC") )
    
    tab=driver.find_element(By.ID, "id_oiss_tab_executive_head")
    tab.click()
    
    ##### EXECUTIVE HEAD
    u.fruns(driver=driver, lib='components.ET_PERSON_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
    
    
    tab=driver.find_element(By.ID, "id_oiss_tab_chairman")
    tab.click()

    
    ##### CHAIRMAN
    u.fruns(driver=driver, lib='components.ET_PERSON_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
    

    
    tab=driver.find_element(By.ID, "id_oiss_tab_contact_person")
    tab.click()

    #### CONTACT PERSON
    u.fruns(driver=driver, lib='components.ET_PERSON_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
    
    
    
    