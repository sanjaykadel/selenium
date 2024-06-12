import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')
    
    fnRun(driver, 'investment.01_login') 
    fnRun(driver, 'investment.02_investment_click') 
    fnRun(driver, 'investment.03_fd_maturation_settlement_click') 
    fnRun(driver, 'investment.03a_fd_maturation_settlement_form_fillup') 
    fnRun(driver, 'investment.04_investment_settlement_click') 
    fnRun(driver, 'investment.04a_investment_settlement_form_fillup') 
    


   