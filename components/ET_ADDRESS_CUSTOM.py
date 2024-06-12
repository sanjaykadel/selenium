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

    curl = f'{u.getUrl()}/?storeName=CONT_SELF_REG_SUBMISSION_NO&_P_PAGE_=entity/components/ET_ADDRESS_CUSTOM.html'
    driver.get(curl)
    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))

    ###### ET_ADDRESS #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")

    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("temprorary")

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
    u.dfn()
