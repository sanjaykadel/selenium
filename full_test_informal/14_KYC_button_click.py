

import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()

    driver = k.get('driver')
    # informal_reg_submission_no = driver.execute_script('return window.localStorage.getItem("BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO");')
    # informal_reg_submission_no = 1689152590

    # curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_informal/cont_informal_reg.html&storeName=BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO&BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO=${informal_reg_submission_no}&user_action=kyc&layoutPath=entity/cont_informal/layout_informal.html'

    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    # driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_content_person")


    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    
   
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_WORK_DETAIL")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_WORK_DETAIL")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))

    form = driver.find_element(By.CLASS_NAME, "table-responsive")
   
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")

    # el = form.find_element(By.NAME, "xsn")
    # el.send_keys("111111")

    # el = form.find_element(By.NAME, "addressId")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)
      

    # el = form.find_element(By.NAME, "districtCd")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = u.ufind_element(driver,form,By.NAME, "vdcCd")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = u.ufind_element(driver,form,By.NAME, "ward")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = u.ufind_element(driver,form,By.NAME, "toleNep")
    # el.send_keys("मारु ")

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_doc")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_DOC")

    # el = form.find_element(By.NAME, "docId")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = form.find_element(By.NAME, "issueNo")
    # el.send_keys("111111")

    # el = u.ufind_element(driver,form,By.NAME, "issueDate")
    # el.send_keys("2007-09-08")
    # u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")


    # el = form.find_element(By.NAME, "issuePlace")
    # el.send_keys("Sanepa")


    # el = u.ufind_element(driver,form,By.NAME, "issueDate")
    # el.send_keys("2007-09-08")
    # u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")


    # el = u.ufind_element(driver,form,By.NAME, "issuePlace")
    # el.send_keys("Sanepa")

    # el = form.find_element(By.NAME, "docfile")
    # el.send_keys(u.sampleFile('tiny.pdf'))
    
    # el = form.find_element(By.NAME, "docbackfile")
    # el.send_keys(u.sampleFile('tiny.pdf'))

    el = form.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_relative_person")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_relative_person")
    # table = form.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    u.dfn()
   
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_relative_person")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_relative_person")
    table = form.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")

    el = u.ufind_element(driver,table,By.NAME, "relId")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
    el = table.find_element( By.NAME, "fnameNep")
    el.send_keys("सुष्मा")

    el = table.find_element(By.NAME, "mnameNep")
    el.send_keys("")
    
    el = table.find_element(By.NAME, "lnameNep")
    el.send_keys("पौडेल")

    el = table.find_element(By.NAME, "fnameEng")
    el.send_keys("Sushma")

    el = table.find_element(By.NAME, "mnameEng")
    el.send_keys("")
    
    el = table.find_element(By.NAME, "lnameEng")
    el.send_keys("Poudel ")

    # el = table.find_element(By.NAME, "dob")
    # el.send_keys("2046-02-02")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")
    
    el = u.ufind_element(driver,form,By.NAME, "gender")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = table.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")
    
    el = table.find_element(By.ID, "id_oiss_kyc_request")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.env_pause()

   
    
    
  

   

    

   
    
   
    
    
   
    

   

   
    
    
    
  

    

    
   
    
