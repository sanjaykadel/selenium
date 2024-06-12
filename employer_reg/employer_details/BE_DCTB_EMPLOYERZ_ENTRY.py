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
        EC.visibility_of_element_located((By.ID, "id_oiss_tab_employer")))

    tab = driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_EMPLOYERZ_ENTRY")

    print(form)

    #
    # print(form.text)
    el = form.find_element(By.NAME, "employerNameEng")

    #print(el)
    #print(el.get_attribute('innerHTML'))
    #print(el.get_attribute('outerHTML'))

    el = form.find_element(By.NAME, "employerNameEng")
    el.send_keys("Nimesh")
    
    el = form.find_element(By.NAME, "employerNameNep")
    el.send_keys("निमेश")

    el = form.find_element(By.NAME, "etypeId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "stypeId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "indZoneCatId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "calendar")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "alertSource")
    el.send_keys("निमेश")

    el = form.find_element(By.NAME, "alertSourceVal")
    el.send_keys("निमेश")

    findButton = driver.find_element( By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_EMPLOYERZ_ENTRY")


    el = findButton.find_element(By.CLASS_NAME, "oiss_save_button")
    el.send_keys(Keys.ENTER)

