import os
# os.environ['oiss_url']= 'https://sstest1.tinker.com.np'
os.environ['oiss_url']= 'http://127.0.0.1:8000'
os.environ['oiss_pause']='1'

 ####   homepage
# fnRun = u.frunInput
# fnRun = u.frun
# u.frun(driver, 'grivence.test',u.frunInput)
#
# u.frun(driver, 'compliance.test',u.frunInput)
# u.frun(driver, 'full_test_self.kyc_button_click',u.frunInput)
# u.frun(driver,'full_test_self.test',u.frunInput)
# u.frun(driver,'full_test_migrant.test',u.frunInput)
# u.frun(driver,'contri_reg.tests',u.frunInput)
# u.frun(driver,'full_test_emp.test',u.frunInput)
# u.frun(driver,'full_test_contri.test',u.frunInput)

# u.frun(driver,'certificate.certificate',u.frunInput)

u.frun(driver, 'mods.ET_DOCS',u.frunInput)
