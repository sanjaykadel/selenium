import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')
    
    fnRun(driver, 'Loan.01_login')
    fnRun(driver, 'Loan.02_loan_click')
    fnRun(driver, 'Loan.03_loan_apply')
    fnRun(driver, 'Loan.03_loan_apply')

   
