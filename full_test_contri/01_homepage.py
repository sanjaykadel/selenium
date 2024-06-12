import os
# os.system('cls')

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

    curl = f'{u.getUrl()}/'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    driver.get(curl)
    u.dfn()
    u.env_pause()

    
    # driver.execute_script('window.localStorage.clear();')

    
   
    
    
    