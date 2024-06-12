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

    curl = f'{u.getUrl()}/?_P_PAGE_=entity/components/ET_CERTIFICATE_CUSTOM.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_CERTIFICATE")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_CERTIFICATE") 
    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = u.ufind_element(driver, form, By.NAME, "fullName")
    el.send_keys("राम")

    el = u.ufind_element(driver, form, By.NAME, "certificateFor")
    el.send_keys("contributor")

    u.ui_send_date(driver=driver,form=form,name="entryDate",value="2050-04-03")


    el = u.ufind_element(driver, form, By.NAME, "location")
    el.send_keys("nepal")

    el = u.ufind_element(driver, form, By.NAME, "holderContact")
    el.send_keys("9999987456")
   
    el = u.ufind_element(driver, form, By.NAME, "holderEmail")
    el.send_keys("rammahat@gmail.com")

    el = u.ufind_element(driver, form, By.NAME, "Description")
    el.send_keys("this ceritificate belong to mr/miss for contributon to the ssf")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    
    element = wait.until(EC.element_to_be_clickable((By.ID, "view")))
    element.send_keys(Keys.ENTER)

    u.dfn()
