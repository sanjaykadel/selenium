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
    surl = 'http://127.0.0.1:8000/?_P_PAGE_=BE_DCTB_ADDRESS_MIGRANT/BE_DCTB_ADDRESS_MIGRANT.html'
    if driver.current_url == surl:
        driver.get(surl)

    ###### BE_DCTB_ADDRESS_MIGRANT #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_ADDRESS_MIGRANT")

    u.dfn()
    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("temprorary")
    
    u.dfn()
    dropdown = form.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    u.dfn()
    dropdown = form.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")
 
    u.dfn()
    dropdown = form.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")
 
    u.dfn()
    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("सफा राखौँ")
 
    u.dfn()
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
