#import fun_utils
#u = fun_utils
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
import time
import inspect
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


# only if debug is on
# with verbocity check

# debug print


def dprint(v, *kwargs):
    print(kwargs, file=sys.stderr)


def msgFrame(back=0):
    # print(dir(inspect))
    frame = inspect.currentframe()

    # todo: use loop
    if back == 1:
        frame = frame.f_back
    if back == 2:
        frame = frame.f_back.f_back

    #previous_frame = inspect.currentframe()[back]
    (filename, line_number,
     function_name, lines, index) = inspect.getframeinfo(frame)
# return (filename, line_number, function_name, lines, index)

    #o=f"""{function_name}| {filename}:{line_number} {function_name}  """
    o = f"""{function_name}| {filename}:{line_number} {function_name}()  """
    # print(o, file=sys.stderr)
    return o

# print file , with v=1


def dfn(*kwargs):
    o = msgFrame(2)
    print(o, file=sys.stderr)


def dfnend(*kwargs):
    print(kwargs[0], file=sys.stderr)

# test err


def terr(**kwargs):
    dfn()
    print(0, msgFrame(0))
    print(1, msgFrame(1))
    print(2, msgFrame(2))
    pass


def err(*kargs, **kwargs):
    fmsg = msgFrame(2)
    print('ERROR: ', fmsg, kargs, kwargs)


# debugsleep to see some output
# disabled in non debug mode
def dsleep(sleep_secs=0):
    if (sleep_secs):
        time.sleep(sleep_secs)
        return
    time.sleep(1)


def dsend_keys(el, keys):
    el.send_keys(keys)
    dsleep(0.2)


def ufind_element(driver, parent, by, key):
    print(key)

    el = parent.find_element(by, key)
    # el.send_keys("")
    # el.location_once_scrolled_into_view
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    ##driver.execute_script("arguments[0].click();", el)
    #action = ActionChains(driver)
    # action.move_to_element(el).perform()
    return el


def ufind_element_scroll(driver, parent, by, key):
    print(key)

    el = parent.find_element(by, key)
    driver.execute_script("arguments[0].scrollIntoView(true)", el)

    return el


def frun(driver, str_lib_file_name, fnRun=None):
    #global driver
    import importlib
    mlib = importlib.import_module(str_lib_file_name)
    importlib.reload(mlib)
    mlib.run(driver=driver, fnRun=fnRun)


def fruns(**kwargs):
    driver = kwargs.get('driver')
    lib = kwargs.get('lib')
    str_lib_file_name = lib

    #driver, str_lib_file_name,fnRun=None
    #global driver
    import importlib
    mlib = importlib.import_module(str_lib_file_name)
    importlib.reload(mlib)
    #mlib.run(driver=driver, fnRun=fnRun)
    mlib.run(**kwargs)


def frunInput(driver, str_lib_file_name, fnRun=None):
    frun(driver, str_lib_file_name, fnRun)
    input(str_lib_file_name + " finished, Press Enter to Continue...")


def sampleFile(filename):
    return os.path.join(os.path.dirname(__file__), 'files', filename)


def getUrl(**kwargs):
    url = "http://127.0.0.1:8000"
    import os
    url = os.environ.get("oiss_url", url)
    return url


def ui_send_date(**kwargs):
    form=kwargs.get("form")
    driver=kwargs.get("driver")
    name=kwargs.get("name")
    value=kwargs.get("value")

    # el = form.find_element(By.NAME, "startDate")
    el = form.find_element(By.NAME,name)
    
    # el.send_keys("2021")
    el.click()
    el=driver.find_element(By.ID,"idTextNpCalendarOiss")
    el.clear()
    # el.send_keys("2080-04-01")
    el.send_keys(value)
    el.send_keys(Keys.ESCAPE)
    el=driver.find_element(By.ID,"idBtnOkCalendarOiss")
    el.click()


def env_pause(**kawrgs):
    import os
    pause = os.environ.get("oiss_pause")
    if pause and pause=='1':
        input("press enter to continue....")
    return pause
    




def main():
    print(sampleFile('tiny.jpg'))

    dfn()
    terr(e="url != curl")
    err(e="url != curl")
    err("url != curl")


if __name__ == '__main__':
    main()
