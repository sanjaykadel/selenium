import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils

click_create=0
def run(**k):
    u.dfn()

    # print('kargs', k)
    driver = k.get('driver')

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/08_contributor_zinformal.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person__save")))
    
     ####### BE_DCTB_PERSON_ZINFORMAL #########
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_PERSON_ZINFORMAL')

     ####### BE_DCTB_CONTRIBUTOR_WORK_DETAIL_ZINFORMAL #########
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_CONTRIBUTOR_WORK_DETAIL_ZINFORMAL')
     ####### BE DCTB ADDRESS2 ZINFORMAL #########
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_ADDRESS2_ZINFORMAL')
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_ADDRESS2_ZINFORMAL')

      ####### BE_DCTB_EMP_DOC1_ZINFORMAL #########
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_EMP_DOC1_ZINFORMAL')
    # u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_EMP_DOC1_ZINFORMAL')

      ####### BE_DCTB_PERSON_Relative_ZINFORMAL #########
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_PERSON_RELATIVE_ZINFORMAL')
    u.frun(driver, 'contributor_informal.cont_informal_detail.BE_DCTB_PERSON_RELATIVE_ZINFORMAL')
