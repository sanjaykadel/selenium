

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
    # curl=f'{u.getUrl()}/?_P_PAGE_=entity\components\BE_OISS_USERS_CUSTOM.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    # driver.get(curl)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
    # informal_reg_submission_no =driver.execute_script('return window.localStorage.getItem("BE_DCTB_ZINFORMAL_REG_SUBMISSION_NO");')



      

    # form = driver.find_element(By.TAG_NAME, "form")
    # input_tag = form.find_element(By.NAME, "username")
    # input_tag.send_keys(informal_reg_submission_no)


    # input_tag = form.find_element(By.NAME, "password")
    # input_tag.send_keys(informal_reg_submission_no)


    # btn = driver.find_element(By.ID, "oiss_id_log_in")
    # btn.click()
     
   
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_ID_CARD")))
    u.dfn()
    
    
    driver.execute_script("window.scrollBy(0, 300);")
    u.dsleep(3)
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_ET_ID_CARD")
    u.dfn()
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_list_add_popup")
    el.send_keys(Keys.ENTER)

    u.dsleep(3)

    el = form.find_element(By.NAME, "employerId")
    el.send_keys("6")

    el = form.find_element(By.NAME, "ownerId")
    el.send_keys("6")

   
    
    # el = form.find_element(By.NAME, "signature")
    # el.send_keys(u.sampleFile('tiny.gif'))

    # el = form.find_element(By.NAME, "signingName")
    # el.send_keys("Sita")

    u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

    el = form.find_element(By.NAME, "name")
    el.send_keys("Sita")

    # u.ui_send_date(driver=driver,form=form,name="dob",value="2080-04-03")

  

    # el = u.ufind_element(driver,form,By.NAME, "countryCode")
    # # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    # el = form.find_element(By.NAME, "startDate")
    # el.click()
    # el=driver.find_element(By.ID,"idTextNpCalenderOiss")
    # el.clear()
    # el.send_keys(Keys.ESCAPE)
    # el.send_keys("2080-04-01")
    # el=driver.find_element(By.ID,"idBtnOkCalenderOiss")
    # el.click()

    
    # el = u.ufind_element(driver, form, By.ID, "idDivNpCalendarOiss")
    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.ID, "idDivNpCalendarOiss")))
    # el = u.ufind_element(driver, form, By.CLASS_NAME, "ndp-nepali-calendar")
    # el.click()
    
    # el = form.find_element(By.NAME, "gender")
    # el.send_keys("Female")

#     el = u.ufind_element(driver,form,By.NAME, "gender")
#     # el.click()
#     el.send_keys(Keys.ARROW_DOWN)
#     el.send_keys(Keys.ENTER)
    
    el = u.ufind_element(driver,form,By.NAME, "bloodgroup")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    
    el = form.find_element(By.NAME, "address")
    el.send_keys("kalimati")

   
    el = form.find_element(By.NAME, "mobileNo")
    el.send_keys("9876543210")

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)

    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_cancel")
    el.send_keys(Keys.ENTER)
    u.env_pause()
    u.dfn()
    u.dsleep(3)
    u.env_pause()