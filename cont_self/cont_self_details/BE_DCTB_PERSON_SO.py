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
    surl = 'http://127.0.0.1:8000/?_P_PAGE_=BE_DCTB_PERSON_SO/BE_DCTB_PERSON_SO.html'
    if driver.current_url == surl:
        driver.get(surl)

    ######## BE_DCTB_PERSON_SO #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_SO")

    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("रमेश")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("प्रसाद")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("नेपाल")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("ramesh")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("prasad")

    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("nepal")

    el = form.find_element(By.NAME, "gender")
    el.send_keys("male")

    el = form.find_element(By.NAME, "dob")
    el.send_keys("2050.09.09")

    dropdown = form.find_element(By.NAME, "countryCode")
    select = Select(dropdown)
    select.select_by_visible_text("nepal")

    # el = form.find_element(By.NAME, "countryCode")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9841786543")

    dropdown = form.find_element(By.NAME, "bloodgroup")
    select = Select(dropdown)
    select.select_by_visible_text("o")

    el = form.find_element(By.NAME, "grandFatherName")
    el.send_keys("Mahesh Nepal")
    el = form.find_element(By.NAME, "fatherName")
    el.send_keys("Umesh Nepal")

    dropdown = form.find_element(By.NAME, "bankId")
    select = Select(dropdown)
    select.select_by_visible_text("nic")

    dropdown = form.find_element(By.NAME, "branchId")
    select = Select(dropdown)
    select.select_by_visible_text("prabhu bank")

    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("Ramesh Nepal")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("54632345456787")

    el = driver.find_element(By.CLASS_NAME, "class_oiss_person_so_save")
    el.send_keys(Keys.ENTER)
    u.dfn()
