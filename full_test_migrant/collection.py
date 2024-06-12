import os

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
        

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_section_form ")))


    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DSTB_COLLECTION_TRAN_HEAD")
    
    u.ui_send_date(driver=driver,form=form,name="form-label",value="2080-04-03")

    el = u.ufind_element(driver,form,By.NAME, "col-auto")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver,form,By.NAME, "col-auto")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)