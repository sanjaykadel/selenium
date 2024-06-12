import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    fnRun = k.get('fnRun')
    driver = k.get('driver')
    # fnRun(driver,'contri_reg.contri_reg_new_emp_home')
    # fnRun(driver, 'contri_reg.contri_reg_new_emp_login')
    # fnRun(driver, 'contri_reg.contri_reg_new_emp_dashboard')   
    fnRun(driver, 'contri_reg.contri_reg_details')
    # fnRun(driver, 'contri_reg.contri_reg_verify_req')
    # fnRun(driver, 'contri_reg.contri_admin_view')
    

