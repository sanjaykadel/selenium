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

    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/4so_contributor_sorojgar.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_person_so_save")))

    ####### BE_DCTB_PERSON_SO #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_SO")

    el = form.find_element(By.NAME, "submissionNo")
    el.send_keys("1234")

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

    dropdown = driver.find_element(By.NAME, "countryCode")
    select = Select(dropdown)
    select.select_by_visible_text("nepal")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("8987364567")

    dropdown = driver.find_element(By.NAME, "bloodgroup")
    select = Select(dropdown)
    select.select_by_visible_text("o")

    el = form.find_element(By.NAME, "grandFatherName")
    el.send_keys("mahesh")

    el = form.find_element(By.NAME, "fatherName")
    el.send_keys("umesh")

    dropdown = driver.find_element(By.NAME, "bankId")
    select = Select(dropdown)
    select.select_by_visible_text("nic")

    dropdown = driver.find_element(By.NAME, "branchId")
    select = Select(dropdown)
    select.select_by_visible_text("prabhu bank")

    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("ramesh nepal")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("9839484838493")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ###### BE_DCTB_CONTRIBUTOR_WORK_DETAIL_SO #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_CONTRIBUTOR_WORK_DETAIL_SO")

    el = form.find_element(By.NAME, "companyName")
    el.send_keys("abc")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("xyz")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9865243678")

    el = form.find_element(By.NAME, "contributionAmount")
    el.send_keys("89765")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ###### BE_DCTB_ADDRESS_SO #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_ADDRESS_SO")

    dropdown = driver.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("temprorary")

    dropdown = driver.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = driver.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = driver.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("टोल")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ###### BE_DCTB_PERSON_DOC_SO #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_DOC_SO")

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("abc")

    el = form.find_element(By.NAME, "issueDate")
    el.send_keys("1290.09.09")

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("xyz")

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "action")
    el.send_keys("action")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_PERSON_SO_RELATIVE #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_SO_RELATIVE")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("रमेश")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("प्रसाद")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("नेपाल")

    el = form.find_element(By.NAME, "dob")
    el.send_keys("2050.09.09")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("ramesh")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("prasad")

    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("nepal")

    el = form.find_element(By.NAME, "gender")
    el.send_keys("male")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("8980364567")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
