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

    # curl = 'http://localhost:8000/?_P_PAGE_=entity/employer/Employer_Entry_Details.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    # # driver.get(curl)

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.ID, "id_oiss_tab_content_contact_person_head")))

       
    tab=driver.find_element(By.ID, "id_oiss_tab_contact_person")
    tab.click()

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_PERSON")


  
    el = form.find_element(By.NAME, "fnameNep")
    el.send_keys("निमेश")

    
    el = form.find_element(By.NAME, "mnameNep")
    el.send_keys("निमेश")

        
    el = form.find_element(By.NAME, "lnameNep")
    el.send_keys("कार्की")

      
    el = form.find_element(By.NAME, "fnameEng")
    el.send_keys("निमेश")

      
    el = form.find_element(By.NAME, "mnameEng")
    el.send_keys("निमेश")

      
    el = form.find_element(By.NAME, "lnameEng")
    el.send_keys("कार्की")

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

        
    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

        
    el = form.find_element(By.NAME, "gender")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

        
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9841522242")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    u.dfn()
