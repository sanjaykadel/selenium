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

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/04_contributor_entry_details.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_SUBMISSION_ZEMP_CONTRIBUTOR_VERIFY_REQUEST")))
    
    u.dfn()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_SUBMISSION_ZEMP_CONTRIBUTOR_VERIFY_REQUEST")

    el = u.ufind_element(driver,form,By.ID, "id_oiss_tab_contri_verify_req")
    el.send_keys(Keys.ENTER)

    u.dfn()
