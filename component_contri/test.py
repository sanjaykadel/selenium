

import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    fnRun = k.get('fnRun')
    driver = k.get('driver')
   

    fnRun(driver, 'Test.Person')
    fnRun(driver, 'components.ET_ADDRESS_CUSTOM')   
    fnRun(driver, 'Test.Doc')  
    fnRun(driver, 'Test.Person')    
    fnRun(driver, 'Test.Person')    
    fnRun(driver, 'Test.Person')    
