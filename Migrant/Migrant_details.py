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

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/MIGRANT.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person_migrant_save")))

    ######## BE_DCTB_PERSON_MIGRANT #########
    u.dfn()
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_PERSON_MIGRANT')

    ###### BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT #########
    u.dfn()
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT')

    ###### BE_DCTB_ADDRESS_MIGRANT #########
    u.dfn()
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_ADDRESS_MIGRANT')
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_ADDRESS_MIGRANT')

    ###### BE_DCTB_PERSON_DOC_MIGRANT #########
    u.dfn()
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_PERSON_DOC_MIGRANT')

    ####### BE_DCTB_PERSON_MIGRANT_RELATIVE #########
    u.dfn()  
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_PERSON_MIGRANT_RELATIVE')
    u.frun(driver, 'Migrant.cont_Migrant_detail.BE_DCTB_PERSON_MIGRANT_RELATIVE')

    u.dfn()