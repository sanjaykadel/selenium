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

    curl = 'http://127.0.0.1:8000/'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "contributor_so")))

    link = driver.find_element(By.CLASS_NAME, "contributor_so")
    link.click()
    u.dsleep()

    link = driver.find_element(By.CLASS_NAME, "contributor_so_login")
    link.click()
    u.dsleep()
