import os

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

    tab=driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()


    #  ##### EMPLOYER
    u.fruns(driver=driver, lib='components.ET_EMPLOYER_CUSTOM',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_EMPLOYER") )
    
    u.dsleep(3)
    
    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()
   
  
    
    ###### ADDRESS
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.ET_ADDRESS1',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS") )
   

    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()


    ##### CONTACT
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.Contact',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_CONTACT") )
    

    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()

    
    #### DOCUMENT
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.Document',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC") )
    

    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_executive_head")
    tab.click()
    
    
    ##### EXECUTIVE HEAD
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.Executive_Head',
        # form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
    )
    

    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_chairman")
    tab.click()

   
    ##### CHAIRMAN
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.Chairman',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
   

    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_contact_person")
    tab.click()

    
    #### CONTACT PERSON
    u.fruns(driver=driver, lib='full_test_emp.Full_Test_Detail.Contact_Person',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON") )
   


    