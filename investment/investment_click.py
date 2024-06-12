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
    u.dfn()

    #print('kargs', k)
    driver = k.get('driver')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "align-middle")))
    curl = f'{u.getUrl()}?_P_PAGE_=entity/investment/ET_INVESTMENT_CUSTOM.html&layoutPath=base_fragment/base.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)
    
    # link=driver.find_element(By.ID, "investment")
    # print('link0',link)
    # link.click()
        
    

    u.dfn()
    u.env_pause()