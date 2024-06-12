import os
#os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils






def profile(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_profile")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON2_CONTRIBUTORZ_PROFILE")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON2_CONTRIBUTORZ_PROFILE")

    el = form.find_element(By.NAME, "fnameNep")
    u.dsend_keys(el,"sanjay")

    el = form.find_element(By.NAME, "lnameNep")
    u.dsend_keys(el,"kadel")



    el = form.find_element(By.NAME, "mnameNep")
    u.dsend_keys(el,"parsad")


    el = form.find_element(By.NAME, "fnameEng")
    u.dsend_keys(el,"sanjay")

    el = form.find_element(By.NAME, "mnameEng")
    u.dsend_keys(el,"parsad ")

    el = form.find_element(By.NAME, "lnameEng")
    u.dsend_keys(el,"kadel")

    el = form.find_element(By.NAME, "dob")
    u.dsend_keys(el,2050)   

    el = form.find_element(By.NAME, "gender")
    u.dsend_keys(el,"M")

    el = form.find_element(By.NAME, "grandFatherName")
    u.dsend_keys(el,"shyam parsad kadel")

    el = form.find_element(By.NAME, "fatherName")
    u.dsend_keys(el,"hari parsad kadel") 



    el = form.find_element(By.NAME, "countryCode")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)
    
    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)
    u.dfn()



def address(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_address")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_ADDRESS2_CONTRIBUTORZ")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_ADDRESS2_CONTRIBUTORZ")


    el = form.find_element(By.NAME, "toleNep")
    u.dsend_keys(el,"dhungadhara")

    el = form.find_element(By.NAME, "toleEng")
    u.dsend_keys(el,"dhungadhara")

    el = form.find_element(By.NAME, "houseNumber")
    u.dsend_keys(el,"12343")

    el = form.find_element(By.NAME, "prakarNoId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "pradeshNoId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "districtCd")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "vdcCd")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "ward")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)

    u.dfn()



def doc(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Doc")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_EMP_DOC1_CONTRIBUTORZ")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_EMP_DOC1_CONTRIBUTORZ")


    el = form.find_element(By.NAME, "issueNo")
    u.dsend_keys(el,1234)


    el = form.find_element(By.NAME, "issuePlace")
    u.dsend_keys(el,"kathmandu")


    el = form.find_element(By.NAME, "issueDate")
    u.dsend_keys(el,2080)

    el = form.find_element(By.NAME, "docId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)
    el = form.find_element(By.NAME, "docfile")
    u.dsend_keys(el,u.sampleFile('tiny.pdf'))

    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)
    u.dfn()


def nominee(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_ Nominee")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON3_CONTRIBUTOR_NOMI")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_PERSON3_CONTRIBUTOR_NOMI")


    el = form.find_element(By.NAME, "fnameNep")
    u.dsend_keys(el,"ramesh")

    el = form.find_element(By.NAME, "lnameNep")
    u.dsend_keys(el,"kadel")



    el = form.find_element(By.NAME, "mnameNep")
    u.dsend_keys(el,"parsad")


    el = form.find_element(By.NAME, "fnameEng")
    u.dsend_keys(el,"ramesh")

    el = form.find_element(By.NAME, "mnameEng")
    u.dsend_keys(el,"parsad")

    el = form.find_element(By.NAME, "lnameEng")
    u.dsend_keys(el,"kadel")

    el = form.find_element(By.NAME, "dob")
    u.dsend_keys(el,2055)   

    el = form.find_element(By.NAME, "gender")
    u.dsend_keys(el,"M")

    el = form.find_element(By.NAME, "grandFatherName")
    u.dsend_keys(el,"tika parsad kadel")

    el = form.find_element(By.NAME, "fatherName")
    u.dsend_keys(el,"shiva raj kadel") 

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bloodgroup")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcType")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcName")
    u.dsend_keys(el,"ramesh kadel") 

    el = form.find_element(By.NAME, "bankAcNumber")
    u.dsend_keys(el,000000000) 

    el = form.find_element(By.NAME, "mobileNo")
    u.dsend_keys(el,9876543210) 
    
    
    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)
    u.dfn()


def dependent(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Dependent_person")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON4_CONTRIBUTOR_DEPENDENT")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON4_CONTRIBUTOR_DEPENDENT")


    
    el = form.find_element(By.NAME, "relId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)




    el = form.find_element(By.NAME, "fnameNep")
    u.dsend_keys(el,"jimmy")

    el = form.find_element(By.NAME, "lnameNep")
    u.dsend_keys(el,"kadel")



    el = form.find_element(By.NAME, "mnameNep")
    u.dsend_keys(el,"parsad")


    el = form.find_element(By.NAME, "fnameEng")
    u.dsend_keys(el,"jimmy")

    el = form.find_element(By.NAME, "mnameEng")
    u.dsend_keys(el,"parsad")

    el = form.find_element(By.NAME, "lnameEng")
    u.dsend_keys(el,"kadel")

    el = form.find_element(By.NAME, "dob")
    u.dsend_keys(el,2030)   

    el = form.find_element(By.NAME, "gender")
    u.dsend_keys(el,"M")

    el = form.find_element(By.NAME, "grandFatherName")
    u.dsend_keys(el,"harka")

    el = form.find_element(By.NAME, "fatherName")
    u.dsend_keys(el,"balen") 

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bloodgroup")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcType")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcName")
    u.dsend_keys(el,"jimmy") 

    el = form.find_element(By.NAME, "bankAcNumber")
    u.dsend_keys(el,000000000) 

    el = form.find_element(By.NAME, "mobileNo")
    u.dsend_keys(el,9876543210) 
    
    
    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)

    u.dfn()

def relative(driver):
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Relative")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON5_CONTRIBUTOR_RELATIVE")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_form_BE_DCTB_PERSON5_CONTRIBUTOR_RELATIVE")


    el = form.find_element(By.NAME, "fnameNep")
    u.dsend_keys(el,"apil")

    el = form.find_element(By.NAME, "lnameNep")
    u.dsend_keys(el,"kadel")



    el = form.find_element(By.NAME, "relId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)



    el = form.find_element(By.NAME, "mnameNep")
    u.dsend_keys(el,"parsad")


    el = form.find_element(By.NAME, "fnameEng")
    u.dsend_keys(el,"apil")

    el = form.find_element(By.NAME, "mnameEng")
    u.dsend_keys(el,"parsad ")

    el = form.find_element(By.NAME, "lnameEng")
    u.dsend_keys(el,"kadel")

    el = form.find_element(By.NAME, "dob")
    u.dsend_keys(el,2056)   

    el = form.find_element(By.NAME, "gender")
    u.dsend_keys(el,"M")

    el = form.find_element(By.NAME, "grandFatherName")
    u.dsend_keys(el,"shankar")

    el = form.find_element(By.NAME, "fatherName")
    u.dsend_keys(el,"ganesh") 

    el = form.find_element(By.NAME, "countryCode")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bloodgroup")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcType")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcName")
    u.dsend_keys(el,"apil") 

    el = form.find_element(By.NAME, "bankAcNumber")
    u.dsend_keys(el,11111111) 

    el = form.find_element(By.NAME, "mobileNo")
    u.dsend_keys(el,1010101010) 
    
    
    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)

    u.dfn()
    
    

def bank(driver):
    u.dfn()
    tab=driver.find_element(By.ID, "id_oiss_tab_contri_Bank")
    tab.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_PERSON2_CONTRIBUTORZ_BANK")))
    form = driver.find_element(By.CLASS_NAME, "class_oiss_gen_content_BE_DCTB_PERSON2_CONTRIBUTORZ_BANK")


    el = form.find_element(By.NAME, "bankAcNumber")
    u.dsend_keys(el,88888888) 

    el = form.find_element(By.NAME, "bankId")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)

    el = form.find_element(By.NAME, "bankAcType")
    el.click();
    u.dsend_keys(el,Keys.ARROW_DOWN)
    u.dsend_keys(el,Keys.ENTER)


    el = form.find_element(By.NAME, "bankAcName")
    u.dsend_keys(el,"ac name") 


    el =form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    u.dsend_keys(el,Keys.ENTER)





    u.dfn()


    



def run(**k):
    u.dfn()

    #print('kargs', k)
    driver = k.get('driver')
        
    curl='http://127.0.0.1:8000/?_P_PAGE_=pages/04_contributor_entry_details.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
    driver.get(curl)


   
    profile(driver)

    
   
    address(driver)
    


    # doc(driver)
    

    nominee(driver)
    
    
    dependent(driver)
    
   
    relative(driver)
    

    bank(driver)

    u.dfn()

  

    return

    u.dfn()


