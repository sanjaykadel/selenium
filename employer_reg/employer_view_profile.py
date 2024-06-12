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
    #print('kargs', k)
    u.dfn()

    driver = k.get('driver')    
  
    curl='http://localhost:8000/?_P_PAGE_=pages/kyc_page/01_employer_view_profile.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "id_oiss_tab_employer")))

    tab=driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()

    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()
    
    tab=driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()

    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()

    u.dfn()
    