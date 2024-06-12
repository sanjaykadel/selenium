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

    driver = k.get('driver')
    
    
    
 
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_CTB_CONTRIBUTOR")))


    ###### ET_EMPLOYER #########
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_BE_CTB_CONTRIBUTOR")
  



    el = form.find_element(By.NAME, "post")
    el.send_keys("Chair person")

    u.ui_send_date(driver=driver,form=form,name="joiningDate",value="2080-04-03")

    el = form.find_element(By.NAME, "groupId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
