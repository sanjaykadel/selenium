
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    fnRun = k.get('fnRun')
    driver = k.get('driver')
   
    fnRun(driver, 'cont_informal_nis.cont_informal_details.ET_PERSON_CUSTOM')
    fnRun(driver, 'cont_informal_nis.cont_informal_details.ET_ADDRESS_CUSTOM')
    fnRun(driver, 'cont_informal_nis.cont_informal_details.ET_BUSINESS_CUSTOM')
    fnRun(driver, 'cont_informal_nis.cont_informal_details.ET_DOC_CUSTOM')
    