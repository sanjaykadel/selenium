import os
#os.system('cls')

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
        
    curl='http://localhost:8000/?_P_PAGE_=pages/admin_page/03a_employer_verify.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "oiss_class_btn_reject")))

    allTag = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_SUBMISSIONZADMIN_CONTRIBUTOR_VERIFY")

    el = allTag.find_element(By.ID, "oiss_class_btn_reject")
    el.send_keys(Keys.ENTER)

    el = allTag.find_element(By.CLASS_NAME, "oiss_class_btn_verify")
    el.send_keys(Keys.ENTER)

    u.dfn()
