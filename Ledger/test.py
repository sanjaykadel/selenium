import os

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    
    driver = k.get('driver')
    fnRun = k.get('fnRun')
    fnRun(driver, 'Ledger.01_login', fnRun)
    fnRun(driver, 'Ledger.02_nav', fnRun)
    fnRun(driver, 'Ledger.03_selectCoa', fnRun)
    fnRun(driver, 'Ledger.04_print', fnRun)
   