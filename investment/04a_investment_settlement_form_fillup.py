
import os

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    
    driver = k.get('driver')
        
    
   
    u.dfn()
    
 
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT_SETTLEMENT")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT_SETTLEMENT")
    u.dfn()
    
    
    form = driver.find_element(By.TAG_NAME, "form")

    el = u.ufind_element(driver,form,By.NAME, "investment")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    input_tag = form.find_element(By.NAME, "party")
    input_tag.send_keys("Product")

    input_tag = form.find_element(By.NAME, "accountNumber")
    input_tag.send_keys("98213123421412")

    input_tag = form.find_element(By.NAME, "shareCertNumber")
    input_tag.send_keys("98213123421412")

    u.ui_send_date(driver=driver,form=form,name="issueDate",value="2080-04-03")

    input_tag = form.find_element(By.NAME, "realizedAmount")
    input_tag.send_keys("10000")

    input_tag = form.find_element(By.NAME, "taxAmount")
    input_tag.send_keys("10000")

    input_tag = form.find_element(By.NAME, "gainLossAmount")
    input_tag.send_keys("10000")
   
    
    el = u.ufind_element(driver,form,By.NAME, "bankId")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    

    u.dsleep(2)


    u.dfn()

    u.env_pause()
    
    ########### SideBar verify click 

   
