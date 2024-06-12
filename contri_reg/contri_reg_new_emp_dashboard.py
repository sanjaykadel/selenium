import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils

u = fun_utils

def run(**k):
    u.dfn()

    driver = k.get('driver')

    driver.get('http://127.0.0.1:8000/?_P_PAGE_=pages/admin_page/2ab_employer_dashboard.html')
    
    curl = 'http://127.0.0.1:8000/?_P_PAGE_=pages/admin_page/2ab_employer_dashboard.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_menu_contributor_entry")))
    btn = driver.find_element(By.CLASS_NAME, "class_oiss_menu_contributor_entry")
    btn.click()


    u.dfn()
