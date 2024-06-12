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

    
    u.dfn()
    u.dsleep(1)
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Bank")
    tab.click()
    u.dfn()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_BANK")))
    
    u.dfn()
   

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_BANK")
    

       

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    el.send_keys(Keys.ENTER)
    el = form.find_element(By.NAME, "bankId")
    el.click()
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "branchId")
    el.click()
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)


    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("Bromish")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("98765432100")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    el.send_keys(Keys.ENTER)
    el = form.find_element(By.NAME, "bankId")
    el.click()
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "branchId")
    el.click()
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)


    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("Bromish")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("98765432100")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)

