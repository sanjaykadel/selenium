import os
# os.environ['oiss_url']= 'https://sstest1.tinker.com.np'
os.environ['oiss_url']= 'http://127.0.0.1:8000'
os.environ['oiss_pause']='1'

 ####   homepage
fnRun = u.frunInput
fnRun = u.frun
u.frun(driver, 'full_test_emp.01_homepage', fnRun)

########################################################
from selenium.webdriver.common.by import By
import employer_reg.employer_reg_new as mlib
import importlib


fnRun = u.frunInput
fnRun = u.frun
u.frun(driver, 'contributor_so.tests', fnRun)

importlib.reload(mlib)
mlib.step1(driver=driver)


# step1();


# todo make new venv for funTestSel
# add requirement.txt there
# activate that venv and run from _start.sh
"""
from selenium.webdriver.common.by import By; print(driver.find_element(By.CLASS_NAME, "oiss_custom_btn_signup"))
from selenium.webdriver.common.by import By; print(driver.find_element(By.CLASS_NAME, "oiss_custom_btn_signup").text)
from selenium.webdriver.common.by import By; print(driver.find_element(By.TAG_NAME, "form").text)

##
print(dir(By))
['CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', 'PARTIAL_LINK_TEXT', 'TAG_NAME', 'XPATH', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

"""


# u.frun(driver, 'employer_reg.employer_reg_new_home')
# u.frun(driver, 'employer_reg.employer_reg_new')
# u.frun(driver, 'employer_reg.employer_reg_new_login_home')
# u.frun(driver, 'employer_reg.employer_reg_new_login')
# u.frun(driver, 'employer_reg.employer_reg_details')


# driver.get('http://localhost:8000/')

link = driver.find_element(By.CLASS_NAME, "employer_reg")
link.click()
input("press enter")


# dropdown-item text-black employer_reg_new

link = driver.find_element(By.CLASS_NAME, "employer_reg_new")
link.click()
input("press enter")


def run(**k):
    u.dfn()

    #print('kargs', k)
    driver = k.get('driver')

    curl = 'http://localhost:8000/?_P_PAGE_=pages/03_employer_entry_details1.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "id_oiss_tab_employer")))

    tab = driver.find_element(By.ID, "id_oiss_tab_employer")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_EMPLOYERZ_ENTRY")

    #
    # print(form.text)
    el = form.find_element(By.NAME, "employerNameEng")
    # print(el)
    # print(el.get_attribute('innerHTML'))
    # print(el.get_attribute('outerHTML'))
    el.send_keys("demo")

    el = form.find_element(By.NAME, "employerNameEng")
    el.send_keys("demo")

    el = form.find_element(By.NAME, "etypeId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    tab = driver.find_element(By.ID, "class_oiss_tab_address")
    tab.click()
    form = driver.find_element(By.ID, "id_oiss_tab_content_address")

    el = form.find_element(By.NAME, "pradeshNoId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    u.dfn()
    
    
    
    
