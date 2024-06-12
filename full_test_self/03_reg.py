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

    curl = f'{u.getUrl()}/?_P_PAGE_=entity/cont_self/cont_self_reg.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_label_ET_PERSON")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_PERSON") 
    el = form.find_element(By.NAME, "imageFile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = u.ufind_element(driver, form, By.NAME, "fnameNep")
    el.send_keys("राम")

    el = u.ufind_element(driver, form, By.NAME, "mnameNep")
    el.send_keys("बहादुर")

    el = u.ufind_element(driver, form, By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form, By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form, By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form, By.NAME, "lnameEng")
    el.send_keys("Thapa")

    el = form.find_element(By.NAME, "countryCode")
    el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    u.ui_send_date(driver=driver,form=form,name="dob",value="2050-04-03")
    

    el = form.find_element(By.NAME, "gender")
    el.send_keys("Male")
    # el.click()
    # u.dsend_keys(el, Keys.ARROW_DOWN)
    # u.dsend_keys(el, Keys.ENTER)
    
    el = form.find_element(By.NAME, "bloodgroup")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "grandFatherName")
    el.send_keys("Hari")

    el = u.ufind_element(driver, form, By.NAME, "fatherName")
    el.send_keys("umesh")

    el = form.find_element(By.NAME, "bankId")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = form.find_element(By.NAME, "branchId")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "bankAcName")
    el.send_keys("ramesh nepal")

    el = u.ufind_element(driver, form, By.NAME, "bankAcNumber")
    el.send_keys("9839484838493")

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")
    
    u.env_pause()

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_WORK_DETAIL")))



    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_WORK_DETAIL")
    
    el = form.find_element(By.NAME, "companyName")
    el.send_keys("Tinker")

    el = form.find_element(By.NAME, "companyAddress")
    el.send_keys("Kathmandu")

    el = form.find_element(By.NAME, "companyContact")
    el.send_keys("9876542312")

  
    el = form.find_element(By.NAME, "contributionAmount")
    el.send_keys("101000")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

   
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_ADDRESS")
    
    table = driver.find_element(
        By.CLASS_NAME, "table-responsive")
       
    
    el = table.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)

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

    u.dsleep(3)

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")       
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
 
    u.dfn() 
    
    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("1234")

    u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-05")
  
    
    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))


    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()

    u.dsleep(3)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
 
    u.dfn() 
    
    el = form.find_element(By.NAME, "issueNo")
    el.send_keys("1234")

    u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-05")
  
    
    el = form.find_element(By.NAME, "docfile")
    el.send_keys(u.sampleFile('tiny.gif'))

    el = form.find_element(By.NAME, "docbackfile")
    el.send_keys(u.sampleFile('tiny.gif'))


    el = form.find_element(By.NAME, "issuePlace")
    el.send_keys("kathmandu")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dfn()
    u.dsleep(3)

    WebDriverWait(driver, 500).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_content_person_relative_so")))


    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_content_person_relative_so")     
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
  
  
    el = u.ufind_element(driver, form, By.NAME, "fnameNep")
    el.send_keys("राम")

    el = u.ufind_element(driver, form, By.NAME, "mnameNep")
    el.send_keys("बहादुर")

    el = u.ufind_element(driver, form, By.NAME, "lnameNep")
    el.send_keys("थापा")

    el = u.ufind_element(driver, form, By.NAME, "fnameEng")
    el.send_keys("ram")

    el = u.ufind_element(driver, form, By.NAME, "mnameEng")
    el.send_keys("Bahadur")

    el = u.ufind_element(driver, form, By.NAME, "lnameEng")
    el.send_keys("Thapa")

    el = u.ufind_element(driver, form, By.NAME, "mobileNo")
    el.send_keys("9898989898")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-05")

    el = u.ufind_element(driver, form, By.NAME, "gender")
    el.send_keys("male")


    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)


