import importlib
import employer_reg.employer_reg_details as mlib
importlib.reload(mlib)
mlib.step1(driver=driver)

"""
import importlib
import employer_reg.employer_reg_new as m1
importlib.reload(m1)
m1.step1(driver=driver)
"""


"""
import employer_reg.employer_reg_new
employer_reg.employer_reg_new.step1(driver=driver)
"""

"""
def test(**k):
	print(k)


test(a=1,b=2)

print(driver)
print('tb',driver)


import importlib
import employer_reg.employer_reg_new as m1
importlib.reload(m1)

#import employer_reg.employer_reg_new
#employer_reg.employer_reg_new.step1(driver=driver)

m1.step1(driver=driver)
"""