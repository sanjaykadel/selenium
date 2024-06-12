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

    

  ####### BE DCTB ADDRESS2 ZINFORMAL #########
    u.dfn()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_ADDRESS2_ZINFORMAL")

    el = u.ufind_element(driver, form,By.NAME, "prakarNoId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    el = u.ufind_element(driver, form,By.NAME, "pradeshNoId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    el = u.ufind_element(driver, form,By.NAME, "districtCd")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    el = u.ufind_element(driver, form,By.NAME, "vdcCd")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    el = u.ufind_element(driver, form,By.NAME, "ward")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    el = u.ufind_element(driver, form,By.NAME, "toleNep")
    el.send_keys("मान गाउँ")
    el = u.ufind_element(driver, form,By.NAME, "toleEng")
    el.send_keys("Man Gau")
    el = u.ufind_element(driver, form,By.NAME, "houseNumber")
    el.send_keys("123")

    
    el = u.ufind_element(driver, form,By.CLASS_NAME, "class_oiss_gen_btn_create")
    if click_create:
        el.send_keys(Keys.ENTER)
        
        u.dfn()