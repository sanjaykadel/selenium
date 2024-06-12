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
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_IMFORMAL_NIS")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("harka")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("sampang")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("rai")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("harka")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("sampang")

    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("rai")

    dropdown = driver.find_element(By.NAME, "countryCode")
    select = Select(dropdown)
    select.select_by_visible_text("nepal")


    el = form.find_element(By.NAME, "dob")
    el.send_keys("2044.03.20")

    el = form.find_element(By.NAME, "gender")
    el.send_keys("male")

    dropdown = driver.find_element(By.NAME, "bloodgroup")
    select = Select(dropdown)
    select.select_by_visible_text("o")

    el = form.find_element(By.NAME, "grandFatherName")
    el.send_keys("shyam lal")

    el = form.find_element(By.NAME, "fatherName")
    el.send_keys("ram lal")

    dropdown = driver.find_element(By.NAME, "bankId")
    select = Select(dropdown)
    select.select_by_visible_text("nic")

    dropdown = driver.find_element(By.NAME, "branchId")
    select = Select(dropdown)
    select.select_by_visible_text("NIC asia")

    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("harka rai")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("7864798362718901")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
