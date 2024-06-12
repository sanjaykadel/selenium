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
    curl = f'{u.getUrl()}/?_P_PAGE_=entity/components/ET_LOAN_CUSTOM.html&layoutPath=base_fragment/base.html'

    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_LOAN")))

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_LOAN") 
    
    link = driver.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    link.click()
    u.dsleep(2)
        
    el = u.ufind_element(driver, form, By.NAME, "ssfId")
    el.send_keys("12345")

    el = u.ufind_element(driver, form, By.NAME, "productName")
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "productType")
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    u.ui_send_date(driver=driver,form=form,name="date",value="2080-04-03")

  

    el = u.ufind_element(driver, form, By.NAME, "daysDifference")
    el.send_keys("25")
    
    el = u.ufind_element(driver, form, By.NAME, "assignedAmount")
    el.send_keys("2500")
    

    el = u.ufind_element(driver, form, By.NAME, "valuatorName")
    el.send_keys("loan")

    el = u.ufind_element(driver, form, By.NAME, "period")
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    u.dsleep(3
             )
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dsleep(2)
    u.dsleep(2)


