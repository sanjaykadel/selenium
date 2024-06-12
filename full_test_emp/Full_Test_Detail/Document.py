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

   

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_DOC")))
   

   
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_document")
    tab.click()

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

    u.env_pause()