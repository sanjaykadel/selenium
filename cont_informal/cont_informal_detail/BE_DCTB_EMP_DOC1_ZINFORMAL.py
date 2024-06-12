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

        ####### BE_DCTB_EMP_DOC1_ZINFORMAL #########
    u.dfn()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_EMP_DOC1_ZINFORMAL")

    el = u.ufind_element(driver, form,By.NAME, "docId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("546789")

    el = form.find_element(By.NAME, "issueDate")
    el.send_keys("1290.09.09")

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = u.ufind_element(driver, form,By.CLASS_NAME, "class_oiss_gen_btn_create")
    if click_create:
        el.send_keys(Keys.ENTER)

    u.dfn()
        