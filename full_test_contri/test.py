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


    ################## full_test_Contributer_emp #########################


    fnRun(driver, 'full_test_contri.01_homepage', fnRun)
    fnRun(driver, 'full_test_contri.02_permanent_employer_login', fnRun)
    fnRun(driver, 'full_test_contri.02_homepage_menu_click', fnRun)

    #fnRun(driver, 'full_test_contri.02_permanent_employer_login', fnRun)
    
    fnRun(driver, 'full_test_contri.03_reg', fnRun)
    
    fnRun(driver, 'full_test_contri.06_save', fnRun)
    fnRun(driver, 'full_test_contri.04_verify_req', fnRun)
    fnRun(driver, 'full_test_contri.07_admin_login', fnRun)
    # fnRun(driver, 'full_test_contri.05_temp_login', fnRun)
    fnRun(driver, 'full_test_contri.08_admin_verify_contri_view', fnRun)
    fnRun(driver, 'full_test_contri.08_admin_verify_contri_view1', fnRun)
    fnRun(driver, 'full_test_contri.09_admin_verify_contri_View', fnRun)
    fnRun(driver, 'full_test_contri.10_admin_verify_contri_click', fnRun)
    fnRun(driver, 'full_test_contri.11_contri_login', fnRun)

    fnRun(driver, 'full_test_contri.12_KYC_click', fnRun)
    fnRun(driver, 'full_test_contri.13_KYC_button_click', fnRun)
    fnRun(driver, 'full_test_contri.14_Change_password', fnRun)
    fnRun(driver, 'full_test_contri.15_Report_click', fnRun)
    fnRun(driver, 'full_test_contri.16_logout', fnRun)
    
    # fnRun(driver, 'idCard.test', fnRun)



    