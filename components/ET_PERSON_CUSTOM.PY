import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import fun_utils
u = fun_utils


def run(**k):
    #print('kargs', k)
    u.dfn()

    driver = k.get('driver')
    # driver.get('http://localhost:8000/?_P_PAGE_=ET_PERSON/ET_PERSON.html&storeName=BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO')

    curl = 'http://127.0.0.1:8000/?storeName=BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO&_P_PAGE_=entity/components/ET_PERSON_CUSTOM.html'
    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")))

    ######  ET_PERSON ############

    u.dfn()
    form = k.get('form')
    if not form:
        form = driver.find_element(

            By.CLASS_NAME, "class_oiss_gen_form_ET_PERSON")

    el = form.find_element(By.NAME, "personType")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = u.ufind_element(driver, form, By.NAME, "fnameNep")
    el.send_keys("राम")

    el = u.ufind_element(driver, form, By.NAME, "mnameNep")
    el.send_keys("बहादुर")

    el = u.ufind_element(driver, form, By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form, By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form, By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form, By.NAME, "lnameEng")
    el.send_keys("Thapa")

    el = form.find_element(By.NAME, "countryCode")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

    el = form.find_element(By.NAME, "gender")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)


    el = form.find_element(By.NAME, "bloodgroup")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "grandFatherName")
    el.send_keys("Hari")

    el = u.ufind_element(driver, form, By.NAME, "fatherName")
    el.send_keys("umesh")

    el = form.find_element(By.NAME, "bankId")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = form.find_element(By.NAME, "branchId")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "bankAcName")
    el.send_keys("ramesh nepal")

    el = u.ufind_element(driver, form, By.NAME, "bankAcNumber")
    el.send_keys("9839484838493")

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
