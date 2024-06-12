
import os
# os.system('cls')

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
    # curl = f'{u.getUrl()}/?_P_PAGE_=entity/contri_emp/contributor_admin_verify.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    # driver.get(curl)
    BE_DCTB_CONTRI_REG_SUBMISSION_NO = driver.execute_script('return window.localStorage.getItem("BE_DCTB_CONTRI_REG_SUBMISSION_NO");')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID,"verify" +BE_DCTB_CONTRI_REG_SUBMISSION_NO)))


    allTag = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_SUBMISSION")


    el = allTag.find_element(By.ID, "view" +  BE_DCTB_CONTRI_REG_SUBMISSION_NO)
    el.send_keys(Keys.ENTER)



    u.dfn()
    u.env_pause()
    


    
    
    

    
    
    
    
    
    