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


    ################## full_test_emp #########################
    fnRun(driver, 'full_test_emp.01_homepage', fnRun)                    ### Homepage
    fnRun(driver, 'full_test_emp.02_homepage_menu_click', fnRun)         ### Homepage Menu Click
    fnRun(driver, 'full_test_emp.03_reg', fnRun)                         ### Registration
    fnRun(driver, 'full_test_emp.04_verify_req', fnRun)                  ### Click Verify Request
    fnRun(driver, 'full_test_emp.05_temp_login', fnRun)                  ### Temporary Login
    fnRun(driver, 'full_test_emp.06_save', fnRun)                        ### Save Click
    fnRun(driver, 'full_test_emp.07_admin_login', fnRun)                 ### Admin Login Page
    fnRun(driver, 'full_test_emp.08_admin_verify_emp_view', fnRun)       ### View Page
    fnRun(driver, 'full_test_emp.10_admin_verify_emp_click', fnRun)      ### Admin Verify Click 
    fnRun(driver, 'full_test_emp.11_emp_login', fnRun)                   ### Permanent Login
    
    # ######### For KYC ###########################################
    fnRun(driver, 'full_test_emp.12_KYC_click', fnRun)
    fnRun(driver, 'full_test_emp.13_KYC_button_click', fnRun)

    # # ########### BY form ########################################
    # fnRun(driver, 'full_test_emp.14_from_contri', fnRun)

   
    #########  collection #######################################
    fnRun(driver, 'full_test_emp.26_collection', fnRun)   

    #########  change password ###################################
    fnRun(driver, 'full_test_emp.27_changePassword', fnRun)                   
    

    ########## For report ######################################
   
    fnRun(driver, 'full_test_emp.Report.15_Report_click', fnRun)
    fnRun(driver, 'full_test_emp.Report.16_TranscationHead', fnRun)
    fnRun(driver, 'full_test_emp.Report.17_TranscationDetail', fnRun)
    fnRun(driver, 'full_test_emp.Report.18_Transcation', fnRun)
    fnRun(driver, 'full_test_emp.Report.19_Interest', fnRun)
    fnRun(driver, 'full_test_emp.Report.20_Balance', fnRun)
    fnRun(driver, 'full_test_emp.Report.21_logout', fnRun)



    # fnRun(driver, 'full_test_emp.Report.16_Report_click_coll', fnRun)
    # fnRun(driver, 'full_test_emp.Report.17_Report_click_reg', fnRun)
    # fnRun(driver, 'full_test_emp.Report.18_Report_contributorstatus', fnRun)
    # fnRun(driver, 'full_test_emp.Report.19_Report_Employeelist', fnRun)
    # fnRun(driver, 'full_test_emp.Report.20_Report_submissionstatus', fnRun)
    # fnRun(driver, 'full_test_emp.Report.21_Report_collection_detail', fnRun)
    # fnRun(driver, 'full_test_emp.Report.22_Report_collection_status', fnRun)
    # fnRun(driver, 'full_test_emp.Report.23_Report_employerSummary', fnRun)
    # fnRun(driver, 'full_test_emp.Report.24_Report_ContributorSummary', fnRun)
    # fnRun(driver, 'full_test_emp.Report.25_Report_ActiveList', fnRun)



    
    




