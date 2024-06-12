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
    surl = 'http://127.0.0.1:8000/?_P_PAGE_=BE_DCTB_PERSON_DOC_SO/BE_DCTB_PERSON_DOC_SO.html'
    if driver.current_url == surl:
        driver.get(surl)

    ###### BE_DCTB_PERSON_DOC_SO #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_DOC_SO")

    dropdown = form.find_element(By.NAME, "docId")
    select = Select(dropdown)
    select.select_by_visible_text("citizen")

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("546789")

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "issueDate")
    el.send_keys("1290.09.09")

    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
