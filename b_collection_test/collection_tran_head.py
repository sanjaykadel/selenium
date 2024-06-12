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

    # print('kargs', k)
    driver = k.get('driver')

    curl = f'{u.getUrl()}/?_P_PAGE_=entity/collection/collection_tran_head.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')

    driver.get(curl)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.ID, "id_oiss_save")))

    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_BE_DSTB_COLLECTION_TRAN_HEAD")

    u.ui_send_date(driver=driver, form=form,
                   name="entryDate", value="2080-04-03")

    # input_tag = form.find_element(By.NAME, "entryDate")
    # input_tag.send_keys("2070.09.09")

    el = form.find_element(By.NAME, "collYear")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    dropdown = form.find_element(By.NAME, "collYear")
    select = Select(dropdown)
    select.select_by_visible_text("2080")

    # el = form.find_element(By.NAME, "collMonth")
    # el.click()
    # u.dsend_keys(el, Keys.ARROW_DOWN)
    # u.dsend_keys(el, Keys.ENTER)

    dropdown = form.find_element(By.NAME, "collMonth")
    select = Select(dropdown)
    select.select_by_visible_text("बैशाख")

    # el = form.find_element(By.NAME, "groupId")
    # el.click()
    # u.dsend_keys(el, Keys.ARROW_DOWN)
    # u.dsend_keys(el, Keys.ENTER)

    dropdown = form.find_element(By.NAME, "groupId")
    select = Select(dropdown)
    select.select_by_visible_text("1")

    # div_element = driver.find_element(
    #     By.ID, "class_oiss_select_contributor_ssfid")
    # el = div_element.find_element(By.NAME, "groupId")
    # el.click()
    # u.dsend_keys(el, Keys.ARROW_DOWN)
    # u.dsend_keys(el, Keys.ENTER)

    btn = driver.find_element(By.ID, "id_oiss_load")
    btn.click()

    # btn = driver.find_element(By.ID, "id_oiss_save")
    # btn.click()

    # btn = driver.find_element(By.ID, "id_oiss_verify")
    # btn.click()

    # btn = driver.find_element(By.ID, "id_oiss_verify")
    # btn.click()

    u.dfn()
