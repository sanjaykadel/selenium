import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')

    fnRun(driver, 'full_test_self.01_homepage')
    fnRun(driver, 'full_test_self.02_homepage_menu_click')
    fnRun(driver, 'full_test_self.03_reg')
    fnRun(driver, 'full_test_self.save')
    fnRun(driver, 'full_test_self.temp_login')
    fnRun(driver, 'full_test_self.verify_req')
    fnRun(driver, 'full_test_self.admin_login')
    fnRun(driver, 'full_test_self.admin_verify_self_page')
    fnRun(driver, 'full_test_self.admin_verify_self_view')
    # fnRun(driver, 'full_test_self.admin_verify_self_query')
    fnRun(driver, 'full_test_self.admin_verify_click')
    fnRun(driver, 'full_test_self.emp_login')
    fnRun(driver, 'full_test_self.kyc')
    fnRun(driver, 'full_test_self.clk_kyc')
    fnRun(driver, 'full_test_self.26_ChangePassword_click')
    fnRun(driver, 'full_test_self.27_Collection_menu_click')
    fnRun(driver, 'full_test_self.15_Report_menu_click')
    fnRun(driver, 'full_test_self.15a_Report_transaction_head_click')
    fnRun(driver, 'full_test_self.15ai_Report_transaction_headdetail_click')
    fnRun(driver, 'full_test_self.15b_Report_transaction_report_click')
    fnRun(driver, 'full_test_self.15c_Report_interest_click')
    fnRun(driver, 'full_test_self.15d_Report_balance_click')

    
    # fnRun(driver, 'full_test_self.16_Report_collection_click')
    # fnRun(driver, 'full_test_self.17_Report_registration_click')
    # fnRun(driver, 'full_test_self.18_Report_selfStatus_click')
    # fnRun(driver, 'full_test_self.19_Report_employeeList_click')
    # fnRun(driver, 'full_test_self.20_Report_submission_click')
    # fnRun(driver, 'full_test_self.21_Report_CollectionDetail_click')
    # fnRun(driver, 'full_test_self.22_Report_CollectionStatus_click')
    # fnRun(driver, 'full_test_self.23_Report_EmployerSummary_click')
    # fnRun(driver, 'full_test_self.24_Report_ContributorSummary_click')
    # fnRun(driver, 'full_test_self.25_Report_ContributorActiveList_click')
        
# 01_homepage.py
# 02_homepage_menu_click.py
# 03_reg.py
# save.py
# temp_login.py
# verify_req.py
# admin_login.py
# admin_verify_emp_page.py
# admin_verify_emp_view.py
# admin_verify_emp_query.py
# admin_verify_emp_click.py
# emp_login.py
