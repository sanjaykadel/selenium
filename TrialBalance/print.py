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

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_GENERAL")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "trial-balance")
    u.dfn()
    u.dsleep(2)
    button = form.find_element(By.ID, "button")
    u.dfn()
    u.dsleep(2)
    button.click()

 