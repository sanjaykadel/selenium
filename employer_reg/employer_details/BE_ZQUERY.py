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

    curl = 'http://localhost:8000/?_P_PAGE_=pages/03_employer_entry_details1.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "id_oiss_tab_query")))

    tab = driver.find_element(By.ID, "id_oiss_tab_query")
    tab.click()

    ####### BE_ZQUERY #########

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_ZQUERY")

    tab=driver.find_element(By.ID, "id_oiss_tab_query")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_ZQUERY")

    el = form.find_element(By.NAME, "query")
    el.send_keys("query 321")
        
    el = form.find_element(By.NAME, "status")
    el.send_keys("status 321")

    el = form.find_element(By.NAME, "fromdate")
    el.send_keys("fromdate 321")

    el = form.find_element(By.NAME, "todate")
    el.send_keys("todate 321")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()