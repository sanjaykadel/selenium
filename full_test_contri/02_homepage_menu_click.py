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
    # curl = f'{u.getUrl()}/'
    u.dfn()

    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "contributor-register")))
    u.dfn()
    link = driver.find_element(By.CLASS_NAME, "contributor-register")
    link.click()
    u.dfn()

    
    link = driver.find_element(By.CLASS_NAME, "form")
    link.click()
    u.dfn()
    u.dsleep()

    u.dfn()
    u.env_pause()
