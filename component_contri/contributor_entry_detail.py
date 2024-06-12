


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

    driver = k.get('driver')
    driver.get(r'http://127.0.0.1:8000/?_P_PAGE_=entity\contri_emp\04_contributor_entry_details.html')

run()  





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
    frun=k.get('frun')

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=entity\contri_emp\04_contributor_entry_details.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))


    u.frun(driver, 'components.ET_PERSON_CUSTOM')
    u.frun(driver, 'components.ET_WORK_DETAIL_CUSTOM')
    u.frun(driver, 'components.ET_ADDRESS_CUSTOM')
    u.frun(driver, 'components.ET_DOC_CUSTOM')
    # u.frun(driver, 'components.ET_RELATIVE)

    

    return