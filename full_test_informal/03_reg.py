

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

    # curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_informal/cont_informal_reg.html'

    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    # driver.get(curl)

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    # driver.execute_script('window.localStorage.clear();')
    # driver.get(curl)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_content_person")


   
    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("Sita")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("kumari")
    
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("Poudel")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("सीता")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("कुमारी")
    
    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("पौडेल ")

    el = u.ufind_element(driver,form,By.NAME, "countryCode")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    # el = form.find_element(By.NAME, "startDate")
    # el.click()
    # el=driver.find_element(By.ID,"idTextNpCalenderOiss")
    # el.clear()
    # el.send_keys(Keys.ESCAPE)
    # el.send_keys("2080-04-01")
    # el=driver.find_element(By.ID,"idBtnOkCalenderOiss")
    # el.click()

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

    # el = u.ufind_element(driver, form, By.ID, "idDivNpCalendarOiss")
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.ID, "idDivNpCalendarOiss")))
    # el = u.ufind_element(driver, form, By.CLASS_NAME, "ndp-nepali-calendar")
    # el.click()
    
    # el = form.find_element(By.NAME, "gender")
    # el.send_keys("Female")

    el = u.ufind_element(driver,form,By.NAME, "gender")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    
    el = u.ufind_element(driver,form,By.NAME, "bloodgroup")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "grandFatherName")
    el.send_keys("Hari")

    el = form.find_element(By.NAME, "fatherName")
    el.send_keys("Shyam")

    el = u.ufind_element(driver,form,By.NAME, "bankId")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver,form,By.NAME, "branchId")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcName")
    el.send_keys("Saving")

    el = form.find_element(By.NAME, "bankAcNumber")
    el.send_keys("12345678901234")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.env_pause()
    u.dfn()
    u.dsleep(3)
    u.env_pause()

    
   
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_WORK_DETAIL")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_WORK_DETAIL")
    
    el = form.find_element(By.NAME, "companyName")
    el.send_keys("Meraki")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("Balaju")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9876543210")

    el = form.find_element(By.NAME, "contributionAmount")
    el.send_keys("111111111")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")
    
    table = driver.find_element(
        By.CLASS_NAME, "table-responsive")
       
    
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("temporary")

    dropdown = form.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = form.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = form.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("सफा राखौँ")

   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)

    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

    dropdown = form.find_element(By.NAME, "addressId")
    select = Select(dropdown)
    select.select_by_visible_text("permanent")

    dropdown = form.find_element(By.NAME, "districtCd")
    select = Select(dropdown)
    select.select_by_visible_text("kathmandu")

    dropdown = form.find_element(By.NAME, "vdcCd")
    select = Select(dropdown)
    select.select_by_visible_text("Kathmandu Metropolitan City")

    dropdown = form.find_element(By.NAME, "ward")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    el = form.find_element(By.NAME, "toleNep")
    el.send_keys("सफा राखौँ")

   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.env_pause()

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    # form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")

    # el = form.find_element(By.NAME, "xsn")
    # el.send_keys("111111")

   
   

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ADDRESS")))
    
    # form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")

    # el = form.find_element(By.NAME, "xsn")
    # el.send_keys("111111")

    
  

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_doc")))

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")
    
    # table = driver.find_element(
    #     By.CLASS_NAME, "table-responsive")
       
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
 
  ##### ET_DOC  ###
    u.dfn() 
    
    dropdown = form.find_element(By.NAME, "docId")
    select = Select(dropdown)
    select.select_by_visible_text("card")

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("546789")

   
    
    u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")
  
    
    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)
    u.dfn()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
 
 
    
    dropdown = form.find_element(By.NAME, "docId")
    select = Select(dropdown)
    select.select_by_visible_text("citizen")

    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("546789")

   
    
    u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")
  
    
    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    
    
    u.dfn() 
    u.dsleep(3)
    u.env_pause()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_relative_person")))

    form = driver.find_element(By.CLASS_NAME, "class_oiss_relative_person")
    # el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    # el.send_keys(Keys.ENTER)
    # u.dfn()
    table = form.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")
    table = form.find_element(By.CLASS_NAME, "table-responsive")
   
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    u.dfn()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_relative_person")))
    
    form = driver.find_element(By.CLASS_NAME, "class_oiss_relative_person")
    table = form.find_element(By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")

    el = table.find_element(By.NAME, "relId")
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
    
    el = table.find_element(By.NAME, "gender")
    el.send_keys("Female")

    el = table.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")
    
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()

    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.env_pause()

   
    
    
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_ZQUERY")))
    # u.dfn()
    # form = driver.find_element(
    #     By.CLASS_NAME, "class_oiss_gen_content_BE_ZQUERY")
    
  

    # el = form.find_element(By.NAME, "query")
    # el.send_keys("111111")

    # el = form.find_element(By.NAME, "status")
    # el.send_keys("good")

    # el = form.find_element(By.NAME, "fromdate")
    # el.send_keys("2046-09-08")

    # el = form.find_element(By.NAME, "todate")
    # el.send_keys("2003-09-07")

    # el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    # el.send_keys(Keys.ENTER)
    # u.dfn()

   
    # el = driver.find_element(By.ID, "id_oiss_verify_request")
    # el.send_keys(Keys.ENTER)

   
    u.dfn()
    u.env_pause()


    
