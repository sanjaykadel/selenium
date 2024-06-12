import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')

 
    fnRun(driver, 'mods.components.ET_PERSONS_MOD')
 