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

    curl = f'{u.getUrl()}/?_P_PAGE_=BE_DSTB_COLLECTION_TRAN_HEAD/BE_DSTB_COLLECTION_TRAN_HEAD.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_DSTB_COLLECTION_TRAN_HEAD")))

    ####### BE_DCTB_PERSON_SO #########
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_content_BE_DSTB_COLLECTION_TRAN_HEAD")

    # el = u.ufind_element(driver,form,By.NAME, "submissionNo")
    # el.send_keys("1234")

    el = u.ufind_element(driver,form,By.NAME, "entryDate")
    el.send_keys("25DEC")

    el = u.ufind_element(driver,form,By.NAME, "collYear")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    # select.select_by_visible_text("Jan")
    # el = form.find_element(By.NAME, "pradeshNoId")
    # el.click()
    # el.send_keys(Keys.ARROW_DOWN)
    # el.send_keys(Keys.ENTER)

    el = u.ufind_element(driver,form,By.NAME, "collMonth")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    div = driver.find_element(
        By.ID, "class_oiss_select_contributor_ssfid")
    
    u.dsleep()
    el =u.ufind_element(driver,div,By.NAME, "groupId")
    # el.click()
    el.send_keys(Keys.ARROW_DOWN)
    el.send_keys(Keys.ENTER)

    btn1 = driver.find_element(By.ID, "id_oiss_load")
    btn1.send_keys(Keys.ENTER)


  

    
    u.dfn()
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_list_contributor_ssfid")
    
    
    tab=driver.find_element(By.ID, "id_oiss_submission_0")
    # tab.click()
    tab.send_keys("2")
   
    

    tab=driver.find_element(By.ID, "id_oiss_pSsid_0")
    tab.send_keys("1")
    # tab.click()
    
    tab=driver.find_element(By.ID, "id_oiss_Cname_0")
    # tab.click()
    tab.send_keys("Ram")

    tab=driver.find_element(By.ID, "id_oiss_Salary_0")
    # tab.click()
    tab.send_keys("1000")

    tab=driver.find_element(By.ID, "id_oiss_remark_0")
    # tab.click()
    tab.send_keys("nice")

    tab=driver.find_element(By.ID, "id_oiss_acfgap_0")
    # tab.click()
    tab.send_keys("acfgap1")

    tab=driver.find_element(By.ID, "id_oiss_transfer_0")
    # tab.click()
    tab.send_keys("1000")

    tab=driver.find_element(By.ID, "id_oiss_totalamount_0")
    # tab.click()
    tab.send_keys("1000")

 
    tab=driver.find_element(By.ID, "id_oiss_submission_1")
    tab.send_keys("2")
    # tab.click()
    

    tab=driver.find_element(By.ID, "id_oiss_pSsid_1")
    # tab.click()
    tab.send_keys("2")
    
    tab=driver.find_element(By.ID, "id_oiss_Cname_1")
    # tab.click()
    tab.send_keys("Sita")

    tab=driver.find_element(By.ID, "id_oiss_Salary_1")
    # tab.click()
    tab.send_keys("2000")

    tab=driver.find_element(By.ID, "id_oiss_remark_1")
    # tab.click()
    tab.send_keys("good")

    tab=driver.find_element(By.ID, "id_oiss_acfgap_1")
    # tab.click()
    tab.send_keys("acfgap2")

    tab=driver.find_element(By.ID, "id_oiss_transfer_1")
    # tab.click()
    tab.send_keys("2000")

    tab=driver.find_element(By.ID, "id_oiss_totalamount_1")
    # tab.click()
    tab.send_keys("2000")


    btn1 = driver.find_element(By.ID, "id_oiss_save")
    btn1.send_keys(Keys.ENTER)

    btn2 = driver.find_element(By.ID, "id_oiss_verify")
    btn2.send_keys(Keys.ENTER)

    btn2 = driver.find_element(By.ID, "id_oiss_interest")
    btn2.send_keys(Keys.ENTER)


    driver.execute_script('window.localStorage.clear();')


    u.dfn()
