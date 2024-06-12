

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
   

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_WORK_DETAIL")))
  

    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_WORK_DETAIL")
    

    # el = u.ufind_element(driver,form,By.NAME, "countryCode")
    # # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)


    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()