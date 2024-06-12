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
    frun = k.get('frun')

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=entity/cont_self/cont_self_reg.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))

    ######## ET_PERSON #########
    u.fruns(driver=driver, lib='components.ET_PERSON_CUSTOM')
    ###### ET_WORK_DETAIL #########
    u.fruns(driver=driver, lib='components.ET_WORK_DETAIL_CUSTOM')
    ###### ET ADDRESS #########
    u.fruns(driver=driver, lib='components.ET_ADDRESS_CUSTOM')
    ###### ET_DOC #########
    u.fruns(driver=driver, lib='components.ET_DOC_CUSTOM')
    ####### ET_PERSON #########
    u.fruns(driver=driver, lib='components.ET_PERSON_CUSTOM')
    return
