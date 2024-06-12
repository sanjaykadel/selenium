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

    curl = f'{u.getUrl()}/?_P_PAGE_=ET_AC_BL/ET_AC_BL.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_AC_BL")))

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_AC_BL") 

    el = u.ufind_element(driver, form, By.NAME, "acName")
    el.send_keys("Bikash")

    el = u.ufind_element(driver, form, By.NAME, "amount")
    el.send_keys("100000")

    u.ui_send_date(driver=driver,form=form,name="date",value="2080-04-03")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)


   