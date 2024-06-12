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
    driver.execute_script("window.scrollBy(0, -300);")

    u.dsleep(3)

    u.dfn()
    # curl=f'{u.getUrl()}/?_P_PAGE_=entity\components\BE_OISS_USERS_CUSTOM.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    # driver.get(curl)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    # emp_reg_submission_no = 1691484655

    # form = driver.find_element(By.TAG_NAME, "form")
    # input_tag = form.find_element(By.NAME, "username")
    # input_tag.send_keys(emp_reg_submission_no)


    # input_tag = form.find_element(By.NAME, "password")
    # input_tag.send_keys(emp_reg_submission_no)


    # btn = driver.find_element(By.ID, "oiss_id_log_in")
    # btn.click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "contributor-register")))


    link=driver.find_element(By.CLASS_NAME,"contributor-register")
    print('link0',link)
    link.click()
    u.dsleep(3) 
    u.dfn()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "form")))


    link=driver.find_element(By.CLASS_NAME,"form")
    print('link0',link)
    link.click()
    u.dsleep(3) 
    u.dfn()
    u.dfn()

   
   
    # #####Clear the localstorage
    

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_profile")
    tab.click()
    
  
     ##### PERSON
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.ET_PERSON_CUSTOM',)
    u.dsleep(3)  
    driver.execute_script("window.scrollBy(0, -300);")

    u.dsleep(3)

    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_address")
    tab.click()
    
    
    ###### ADDRESS
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.ET_ADDRESS1',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS") )
    u.dsleep(3) 

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Doc")
    tab.click()
    
    u.dsleep(3) 
    #### DOCUMENT
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.Document',
        form=driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC") )
    u.dsleep(3)

    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Relative")
    tab.click()
 
    ##### Relative
    u.fruns(driver=driver, lib='full_test_contri.Full_Test_Detail.Relative',
        form=driver.find_element(By.ID, "id_oiss_content_contri_Relative") )
    
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
    

    
   
