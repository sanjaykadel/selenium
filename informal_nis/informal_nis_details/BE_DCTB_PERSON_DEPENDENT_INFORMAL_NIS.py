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
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON_DEPENDENT_INFORMAL_NIS")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("महेश")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("प्रसाद")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("नेपाल")

    el = form.find_element(By.NAME, "dob")
    el.send_keys("2050.09.09")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("mahesh")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("prasad")

    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("nepal")

    el = form.find_element(By.NAME, "gender")
    el.send_keys("male")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9865436789")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()