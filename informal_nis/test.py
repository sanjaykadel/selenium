import fun_utils
u = fun_utils
def run(**k):
    u.dfn()
    fnRun = k.get('fnRun')
    driver = k.get('driver')

    
    fnRun(driver, 'informal_nis.informal_nis_details_save')