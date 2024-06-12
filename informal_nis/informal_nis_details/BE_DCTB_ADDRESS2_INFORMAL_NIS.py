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

    curl = 'http://localhost:8000/?_P_PAGE_=pages/Z13_informal.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    
    driver.get(curl)
    u.dfn()


    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_ADDRESS2_INFORMAL_NIS")
    
    dropdown = driver.find_element(By.NAME, "prakarNoId")
    select = Select(dropdown)
    select.select_by_visible_text("permanent")

    dropdown = driver.find_element(By.NAME, "pradeshNoId")
    select = Select(dropdown)
    select.select_by_visible_text("state1")

    dropdown = driver.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = driver.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = driver.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("Milan Chowk")

    el = form.find_element(By.NAME, "toleEng")
    el.send_keys("Milan Chowk")

    el = form.find_element(By.NAME, "houseNumber")
    el.send_keys("29")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()