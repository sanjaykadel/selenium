
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
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT_FD")))
    u.dfn()
   
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT_FD")
    u.dfn()

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "bank")
    input_tag.send_keys("NIC")

    u.ui_send_date(driver=driver,form=form,name="valueDate",value="2080-04-03")

    input_tag = form.find_element(By.NAME, "fdNo")
    input_tag.send_keys("1234")

    input_tag = form.find_element(By.NAME, "refAccountNo")
    input_tag.send_keys("1234")
  
    input_tag = form.find_element(By.NAME, "principalAmount")
    input_tag.send_keys("4000")

    input_tag = form.find_element(By.NAME, "interestRate")
    input_tag.send_keys("12")

    u.ui_send_date(driver=driver,form=form,name="openingDate",value="2080-04-03")

    u.ui_send_date(driver=driver,form=form,name="maturityDate",value="2080-04-03")

    el = u.ufind_element(driver,form,By.NAME, "bankId")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    
    input_tag = form.find_element(By.NAME, "accountNo")
    input_tag.send_keys("98213123421412")
    u.dsleep(2)
    

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    
    u.dsleep(2)


    u.dfn()

    u.env_pause()
    
    ########### SideBar verify click 

   