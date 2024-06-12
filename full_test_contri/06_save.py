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
        
    # curl='http://localhost:8000/?_P_PAGE_=entity/employer/Employer_Entry_Details.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
    # driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "id_oiss_save")))


    form = driver.find_element(
        By.ID, "id_oiss_save")

    el = form.find_element(By.ID, "id_oiss_verify_request")
    el.send_keys(Keys.ENTER)




    u.dfn()