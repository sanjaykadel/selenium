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

    #print('kargs', k)
    driver = k.get('driver')

    curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_migrant/cont_migrant_verify.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    
    driver.get(curl)
