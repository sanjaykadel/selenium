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

    
    u.dfn()
    u.dsleep(1)
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Relative")
    tab.click()
    u.dfn()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "id_oiss_content_contri_Relative")))
    
    u.dfn()
    # tab=driver.find_element(By.ID, "id_oiss_tab_contri_address")
    # tab.click()

    form = driver.find_element(
        By.ID, "id_oiss_content_contri_Relative")
    

       

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    dropdown = form.find_element(By.NAME, "association")
    select = Select(dropdown)
    select.select_by_visible_text("relative")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("राम")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("पौडेल")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("Ram")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("Poudel ")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")
    
    el = form.find_element(By.NAME, "gender")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)


    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    dropdown = form.find_element(By.NAME, "association")
    select = Select(dropdown)
    select.select_by_visible_text("dependent")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("श्याम")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("पौडेल")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("Shyam")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("Poudel ")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")
    
    el = form.find_element(By.NAME, "gender")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)


    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_edit_popup")
    el.send_keys(Keys.ENTER)
    dropdown = form.find_element(By.NAME, "association")
    select = Select(dropdown)
    select.select_by_visible_text("nominee")

    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("सुष्मा")

    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("पौडेल")

    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("Sushma")

    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("")
    
    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("Poudel ")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")
    
    el = form.find_element(By.NAME, "gender")
    el.send_keys("Female")

    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(3)
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.dfn()
    u.dsleep(2)