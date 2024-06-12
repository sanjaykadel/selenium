
import os
#os.system('cls')

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
   
 

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT")))
    u.dfn()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT")))
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_INVESTMENT")
    u.dfn()
    
    u.dfn()  
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    el.send_keys(Keys.ENTER)

    form = driver.find_element(By.TAG_NAME, "form")
    input_tag = form.find_element(By.NAME, "product")
    input_tag.send_keys("Product")

    u.ui_send_date(driver=driver,form=form,name="valueDate",value="2080-04-03")

    input_tag = form.find_element(By.NAME, "portfolio")
    input_tag.send_keys(Keys.ARROW_DOWN)
    input_tag.send_keys(Keys.ENTER)

    input_tag = form.find_element(By.NAME, "partyName")
    input_tag.send_keys("partyName")

    el = u.ufind_element(driver,form,By.NAME, "type")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)
    
    input_tag = form.find_element(By.NAME, "accountNumber")
    input_tag.send_keys("98213123421412")

    input_tag = form.find_element(By.NAME, "refAccount")
    input_tag.send_keys("98213123421412")

    

    input_tag = form.find_element(By.NAME, "period")
    input_tag.send_keys("100days")

    u.ui_send_date(driver=driver,form=form,name="maturityDate",value="2080-04-03")

   

    u.ui_send_date(driver=driver,form=form,name="maturityDateEng",value="2080-04-03")

    input_tag = form.find_element(By.NAME, "amount")
    input_tag.send_keys("1000")
   

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)

    u.dsleep(2)


    u.dfn()

    u.env_pause()
    
    ########### SideBar verify click 

   