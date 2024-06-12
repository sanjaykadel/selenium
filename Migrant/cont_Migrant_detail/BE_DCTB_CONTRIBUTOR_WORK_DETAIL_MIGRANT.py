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
    surl = 'http://127.0.0.1:8000/?_P_PAGE_=BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT/BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT.html'
    if driver.current_url == surl:
        driver.get(surl)

    ###### BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_CONTRIBUTOR_WORK_DETAIL_MIGRANT")

    el = form.find_element(By.NAME, "companyName")
    el.send_keys("Cheeesss")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("xxxx")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9876542312")

    el = form.find_element(By.NAME, "contributionAmount")
    el.send_keys("89765")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
