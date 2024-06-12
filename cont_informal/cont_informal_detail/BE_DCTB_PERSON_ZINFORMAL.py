import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils

click_create=0
def run(**k):
    u.dfn()

    # print('kargs', k)
    driver = k.get('driver')

    surl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/08_contributor_zinformal.html'
    if driver.current_url != surl:
        u.err('driver.current_url != surl')
    driver.get(surl)

   
    
    ####### BE_DCTB_PERSON_ZINFORMAL #########
    u.dfn()
    form = driver.find_element( By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_ZINFORMAL")

   
    el = u.ufind_element(driver, form,By.NAME, "fnameNep")
    el.send_keys("राम")

    el = u.ufind_element(driver, form,By.NAME, "mnameNep")
    el.send_keys("बहादुर")

    el = u.ufind_element(driver, form,By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form,By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form,By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form,By.NAME, "lnameEng")
    el.send_keys("Thapa")

    el = u.ufind_element(driver, form,By.NAME, "gender")
    el.send_keys("male")

    el = u.ufind_element(driver, form,By.NAME, "dob")
    el.send_keys("2050.09.09")

    el= driver.find_element(By.NAME, "countryCode")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el= driver.find_element(By.NAME, "bloodgroup")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver, form,By.NAME, "grandFatherName")
    el.send_keys("Hari")

    el = u.ufind_element(driver, form,By.NAME, "fatherName")
    el.send_keys("umesh")

    el = driver.find_element(By.NAME, "bankId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = driver.find_element(By.NAME, "branchId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver, form,By.NAME, "bankAcName")
    el.send_keys("ramesh nepal")

    el = u.ufind_element(driver, form,By.NAME, "bankAcNumber")
    el.send_keys("9839484838493")

    el = u.ufind_element(driver, form,By.NAME, "mobileNo")
    el.send_keys("9898989898")


    # el = u.ufind_element(driver, form,By.CLASS_NAME, "btn btn-success class_oiss_person__save")
    # if click_create:
    #     el.send_keys(Keys.ENTER)

    u.dfn()
