
import os
#os.system('cls')

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
    curl = f'{u.getUrl()}/?_P_PAGE_=entity\components\ET_WORKAREA_DURATION_CUSTOM.html'

    if driver.current_url == "" or driver.current_url == curl:
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_WORKAREA_DURATION")))
    

    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_WORKAREA_DURATION")
    


    # el = form.find_element(By.NAME, "startDate")
    # # el.send_keys("2021")
    # el.click()
    # el=driver.find_element(By.ID,"idTextNpCalendarOiss")
    # el.clear()
    # el.send_keys("2080-04-01")
    # el.send_keys(Keys.ESCAPE)
    # el=driver.find_element(By.ID,"idBtnOkCalendarOiss")
    # el.click()
    u.ui_send_date(driver=driver,form=form,name="startDate",value="2080-04-03")
    u.ui_send_date(driver=driver,form=form,name="endDate",value="2080-04-05")



    # el = form.find_element(By.NAME, "endDate")
    # el.send_keys("2022")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()

    