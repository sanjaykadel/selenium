import fun_utils
u = fun_utils


def runAll(driver, fnRun):
    u.dfn()
    print("Test: 1 = clear local storage")
    fnRun(driver, 'employer_reg.employer_home_menu')

    print("Test:1b = Employer SignUp")
    fnRun(driver, 'employer_reg.employer_reg_new_home_signup')

    print("Test: 3 = Employer Entry Details")
    fnRun(driver, 'employer_reg.employer_reg_details_save')

    print("Test: 4 = Employer Login")
    fnRun(driver, 'employer_reg.employer_reg_new_home_login')
    fnRun(driver, 'employer_reg.employer_reg_new_login_details')

    print("Test: 5 = Employer View Details")
    fnRun(driver, 'employer_reg.employer_reg_details_view')

    print("Test: 4 = Employer User Verify")
    fnRun(driver, 'employer_reg.emp_reg_new_details_verify')

    print("Test 5: verify employer admin")
    fnRun(driver, 'employer_reg.employer_admin_view')

    print("Test 6: Admin Login")
    fnRun(driver, 'employer_reg.employer_admin_login')
    
    print("Test 7: Permanent Employer Login")
    fnRun(driver, 'employer_reg.employer_permanent_login')

    print("Test 8: Permanent Employer Edit")
    fnRun(driver, 'employer_reg.employer_permanent_save_edit')

    print("Test 9: Permanent Employer View")
    fnRun(driver, 'employer_reg.employer_permanent_save_view')
    
    # print("Test: 5 = employer login rojagaradata")
    # fnRun(driver, 'employer_reg.employer_rojagaradata_new_login_home')
    # fnRun(driver, 'employer_reg.employer_rojagaradata_new_login')
    # fnRun(driver, 'employer_reg.employer_view_profile')
    # fnRun(driver, 'employer_reg.employer_edit_profile')

    # fnRun(driver, 'employer_reg.employer_view_profile')


def run(**k):
    u.dfn()
    driver = k.get('driver')

    fnRun = k.get('fnRun')

    runAll(driver, fnRun)
    # print("Test 8: Permanent Employer Edit")
    # fnRun(driver, 'employer_reg.employer_permanent_save_edit')

    # print("Test 9: Permanent Employer View")
    # fnRun(driver, 'employer_reg.employer_permanent_save_view')

    # fnRun(driver, 'employer_reg.employer_home_menu')

    # fnRun(driver, 'employer_reg.employer_home_menu')
    # fnRun(driver, 'employer_reg.employer_home_menu')
    # fnRun(driver, 'employer_reg.employer_details.BE_ZQUERY')

    # fnRun(driver, 'employer_reg.employer_home_menu')
    fnRun(driver, 'employer_reg.employer_reg_details_save')
