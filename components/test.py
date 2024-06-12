import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')

   
    fnRun(driver, 'components.ET_EMPLOYER_CUSTOM')  
    fnRun(driver, 'components.Cont_Migrant_Detail')
    fnRun(driver, 'components.ET_PERSON_CUSTOM')
    fnRun(driver, 'components.ET_WORK_DETAIL_CUSTOM')
    fnRun(driver, 'components.ET_ADDRESS_CUSTOM')  
    fnRun(driver, 'components.ET_DOC_CUSTOM')  
    