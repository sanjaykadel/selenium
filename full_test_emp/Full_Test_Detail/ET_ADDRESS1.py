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

    driver = k.get('driver')
    

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
   

    ###### ET_ADDRESS #########
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")
    
    table = driver.find_element(
        By.CLASS_NAME, "table-responsive")
       
    
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("temporary")

    dropdown = form.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = form.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = form.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("सफा राखौँ")

   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)

    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("permanent")

    dropdown = form.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = form.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = form.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("सफा राखौँ")

   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.env_pause()