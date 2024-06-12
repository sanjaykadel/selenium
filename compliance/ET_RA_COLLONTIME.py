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

    curl = f'{u.getUrl()}/?_P_PAGE_=ET_RA_COLLONTIME/ET_RA_COLLONTIME.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)
    u.dfn()

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_section_form undefined")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_RA_COLLONTIME") 
    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = u.ufind_element(driver, form, By.NAME, "employerId")
    el.send_keys("11")

    el = u.ufind_element(driver, form, By.NAME, "previousCollection")
    el.send_keys("2021")

    # u.ui_send_date(driver=driver,form=form,name="entryDate",value="2050-04-03")


    el = u.ufind_element(driver, form, By.NAME, "amountCollected")
    el.send_keys("1000")

    el = u.ufind_element(driver, form, By.NAME, "latestCollection")
    el.send_keys("234444")
   
    el = u.ufind_element(driver, form, By.NAME, "delDate")
    el.send_keys("2021")

    el = u.ufind_element(driver, form, By.NAME, "entered")
    el.send_keys("tt")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    

    u.dfn()
