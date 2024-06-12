import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


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

    print(form)

    #
    # print(form.text)
    el = form.find_element(By.NAME, "employerNameEng")

    #print(el)
    #print(el.get_attribute('innerHTML'))
    #print(el.get_attribute('outerHTML'))

    el = form.find_element(By.NAME, "employerNameEng")
    el.send_keys("Nimesh")
    
    el = form.find_element(By.NAME, "employerNameNep")
    el.send_keys("निमेश")

    el = form.find_element(By.NAME, "etypeId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "stypeId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "indZoneCatId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "calendar")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "alertSource")
    el.send_keys("निमेश")

    el = form.find_element(By.NAME, "alertSourceVal")
    el.send_keys("निमेश")

    findButton = driver.find_element( By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_EMPLOYERZ_ENTRY")


    el = findButton.find_element(By.CLASS_NAME, "oiss_save_button")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_ADDRESS1_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_address")
    tab.click()
    form = driver.find_element(By.ID, "id_oiss_tab_content_address")

    el = form.find_element(By.NAME, "pradeshNoId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "prakarNoId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "districtCd")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "vdcCd")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "ward")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("गोकर्ण")
    
    el = form.find_element(By.NAME, "toleEng")
    el.send_keys("gokarna")
        
    el = form.find_element(By.NAME, "houseNumber")
    el.send_keys("25522")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_PERSON_CONTACT1_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_contact")
    tab.click()
    form = driver.find_element(By.ID, "id_oiss_tab_content_person_contact")

    el = form.find_element(By.NAME, "ctypeId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "cValue")
    el.send_keys("nimesh@gmail.com")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_EMP_DOC #########

    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_EMP_DOC")

    el = form.find_element(By.NAME, "docId")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("20500101")

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("Gokarna")

    el = form.find_element(By.NAME, "issueDate")
    el.send_keys("2050:01:01")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    ####### BE_DCTB_PERSON1_EXECUTIVE_HEAD_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_executive_head")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON1_EXECUTIVE_HEAD_EMPLOYERZ")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("निमेश executive head")

    
    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("निमेश executive head")

        
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("कार्की executive head")

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
        
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("98415222422")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_PERSON1_CHAIRMAN_HEAD_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_chairman")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON1_CHAIRMAN_HEAD_EMPLOYERZ")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("निमेश chairman head")
        
    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("निमेश chairman head")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("कार्की chairman head")

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
        
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("98415222422")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_DCTB_PERSON1_CONTACT_PERSON_HEAD_EMPLOYERZ #########

    tab=driver.find_element(By.ID, "id_oiss_tab_contact_person")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON1_CONTACT_PERSON_HEAD_EMPLOYERZ")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("निमेश contact person")
        
    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("निमेश contact person")

    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("कार्की contact person")

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
        
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("98415222422")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    ####### BE_ZQUERY #########

    tab=driver.find_element(By.ID, "id_oiss_tab_query")
    tab.click()
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_ZQUERY")

    el = form.find_element(By.NAME, "query")
    el.send_keys("query 321")
        
    el = form.find_element(By.NAME, "status")
    el.send_keys("status 321")

    el = form.find_element(By.NAME, "fromdate")
    el.send_keys("fromdate 321")

    el = form.find_element(By.NAME, "todate")
    el.send_keys("todate 321")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
