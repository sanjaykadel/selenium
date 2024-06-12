
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
    anchor_tag = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Verify")))
    anchor_tag.click()
    u.dfn()
    u.env_pause()