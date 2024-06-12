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

    #print('kargs', k)
    driver = k.get('driver')

    curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_migrant/cont_migrant_verify.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)
    

   
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_SUBMISSION")))
    migrant_reg_submission_no = driver.execute_script('return window.localStorage.getItem("CONT_MIGRANT_REG_SUBMISSION_NO");')



    allTag = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_SUBMISSION")


    el = allTag.find_element(By.ID, "view" + migrant_reg_submission_no)
    el.send_keys(Keys.ENTER)



    u.dfn()
 
    


    
    
    