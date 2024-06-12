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

    # curl = 'http://localhost:8000/?_P_PAGE_=pages/03_employer_entry_details1.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    # driver.get(curl)

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_CONTACT")))
    

    ####### Contact #########

    tab = driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()

    u.dfn()
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_CONTACT")
    
    u.dfn()

    # table = driver.find_element(
    #     By.CLASS_NAME, "table-responsive")
       
    # u.dfn()
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_list_edit_popup")))
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
       
    u.dfn()
    # el = form.find_element(By.NAME, "ctypeId")
    # el.click();
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    dropdown = form.find_element(By.NAME, "ctypeId")
    select = Select(dropdown)
    select.select_by_visible_text("इमेल")

    el = form.find_element(By.NAME, "cValue")
    el.send_keys("cValue")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_list_edit_popup")))
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
       
    dropdown = form.find_element(By.NAME, "ctypeId")
    select = Select(dropdown)
    select.select_by_visible_text("फोन नम्बर")

    el = form.find_element(By.NAME, "cValue")
    el.send_keys("cValue")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()

    u.env_pause()