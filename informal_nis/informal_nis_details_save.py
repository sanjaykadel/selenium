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

    curl = 'http://localhost:8000/?_P_PAGE_=pages/Z13_informal.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person_informal_nis_save")))
    
     ######## BE_DCTB_PERSON_IMFORMAL_NIS #########
    u.dfn()
    u.frun(driver, 'informal_nis.informal_nis_details.BE_DCTB_PERSON_IMFORMAL_NIS')

    ###### BE_DCTB_ADDRESS2_INFORMAL_NIS #########
    u.dfn()
    u.frun(driver, 'informal_nis.informal_nis_details.BE_DCTB_ADDRESS2_INFORMAL_NIS')

    ###### BE_DCTB_EMP_DOC1_INFORMAL_NIS #########
    u.dfn()
    u.frun(driver, 'informal_nis.informal_nis_details.BE_DCTB_EMP_DOC1_INFORMAL_NIS')

    ###### BE_DCTB_PERSON_DEPENDENT_INFORMAL_NIS #########
    u.dfn()
    u.frun(driver, 'informal_nis.informal_nis_details.BE_DCTB_PERSON_DEPENDENT_INFORMAL_NIS')

    u.dfn()

