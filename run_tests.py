import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    driver = k.get('driver')
    fnRun = k.get('fnRun')

    import os
    # os.environ['oiss_url']= 'https://sstest1.tinker.com.np'
    os.environ['oiss_url']= 'http://127.0.0.1:8000'

    print("Hello write initial test like as of tmpCmdsExample.py in this file ")
    # u.frun(driver,'full_test_emp.test',u.frunInput)
    # # u.frun(driver,'b_collection_test.test',u.frunInput) 
    # u.frun(driver,'full_test_contri.test',u.frunInput)
    # u.frun(driver,'full_test_informal.test',u.frunInput)
    # u.frun(driver,'full_test_migrant.test',u.frunInput)
    # u.frun(driver,'full_test_self.test',u.frunInput)
    # u.frun(driver,'investment.test',u.frunInput)
    u.frun(driver,'modes','ET_EMPLOYERS','emp.test',u.frunInput)

