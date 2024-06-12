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
    fnRun = k.get('fnRun')


    ################## full_test_migrant #########################

    fnRun(driver, 'full_test_migrant.03_reg', fnRun)
    fnRun(driver, 'full_test_migrant.save', fnRun)
    
    fnRun(driver, 'full_test_migrant.verify_req', fnRun)
    fnRun(driver, 'full_test_migrant.temp_login', fnRun)
    fnRun(driver, 'full_test_migrant.admin_login')
    fnRun(driver, 'full_test_migrant.admin_login_verify_click')
    fnRun(driver, 'full_test_migrant.admin_login_migrant_click')
    # fnRun(driver, 'full_test_migrant.admin_verify_page')
    fnRun(driver, 'full_test_migrant.admin_verify_view')
    # fnRun(driver, 'full_test_migrant.admin_verify_query')
    fnRun(driver, 'full_test_migrant.admin_verify_click')
    fnRun(driver, 'full_test_migrant.migrant_login')

    fnRun(driver, 'full_test_migrant.13_KYC_click_menu', fnRun)
    fnRun(driver, 'full_test_migrant.14_KYC_button_click', fnRun)
    fnRun(driver, 'full_test_migrant.15_Report_menu_click', fnRun)
    fnRun(driver, 'full_test_migrant.16_Report_Interest_click', fnRun)
    fnRun(driver, 'full_test_migrant.17_Report_tran_report_click', fnRun)
    fnRun(driver, 'full_test_migrant.18_Report_tran_head_click', fnRun)
    fnRun(driver, 'full_test_migrant.26_ChangePassword_click', fnRun)
    fnRun(driver, 'full_test_migrant.27_Collection_menu_click', fnRun) 
    fnRun(driver, 'full_test_migrant.logout.py', fnRun)


    