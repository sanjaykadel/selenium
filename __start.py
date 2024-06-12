#global driver

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import io
import os
from pathlib import Path
import fun_utils
u = fun_utils

_DEBUG_EXEC_ = True; 
chrome_options = Options()
#chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
#chrome_options.add_argument(r"user-data-dir=C:\Users\ssibro\Desktop\tmp\ChromeProfiles\ProfileChrome")
chrome_options.add_argument(f"user-data-dir={Path.home()}/tmp_chrome_sel")
from selenium import webdriver
PY_CHROME_DRIVER=os.environ.get("PY_CHROME_DRIVER")
if PY_CHROME_DRIVER=="0":

	import chromedriver_autoinstaller
	chromedriver_autoinstaller.install()
elif PY_CHROME_DRIVER=="1":	
	# pip install get-chrome-driver
	from get_chrome_driver import GetChromeDriver
	from selenium import webdriver

	# Install the driver:
	# Downloads ChromeDriver for the installed Chrome version on the machine
	# Adds the downloaded ChromeDriver to path
	get_driver = GetChromeDriver()
	get_driver.install()
elif PY_CHROME_DRIVER=="2":	
	# pip install get-chrome-driver
	from get_chrome_driver import GetChromeDriver
	from selenium import webdriver

	# Install the driver:
	# Downloads ChromeDriver for the installed Chrome version on the machine
	# Adds the downloaded ChromeDriver to path
	get_driver = GetChromeDriver()
	# get_driver.install()
elif PY_CHROME_DRIVER=="3":	
	pass

"""
os.system("start cmd")

C:\vprj\openimis_ssf_sosys230406\funTestSel>where chromedriver
C:\vprj\openimis_ssf_sosys230406\bePyCode\venv\Lib\site-packages\chromedriver_autoinstaller\108\chromedriver.exe
"""

#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\vprj\openimis_ssf_sosys230406\funTestSel\tools\chromedriver.exe')

# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get('http://google.com')

#import myfile
#myfile.cmdStart( {'driver':driver} )


def exit():
	import sys; 
	sys.exit()

if os.environ.get("PY_DEBUG_SHELL_OPEN","0")=="1":
	pass
else:
	exit()

cmd_eval_input=False  #execute 1st without user input
name=''
isXclip=False
import subprocess
while(True):
	try:
		if cmd_eval_input:
			name = input("Input Escaped Eval Code: ")
			print(name)
		cmd_eval_input=True # now will always eval input

		if(name==''):
			if False: 
				# read contents from clipboard and execute it
				runcmd="xclip"
				output = subprocess.check_output(runcmd, shell=True).decode(encoding='utf-8')
				print(output) #from clipboard
				exec(output)
			else:
				# read contents of file and run 
				import os;  ofile = os.path.join(os.path.dirname(__file__),'tmpCmds.py' ); #print(ofile)
				if not os.path.exists(ofile):
					f = open(ofile, "w", encoding='utf8', errors='ignore')
					f.write('print("Hello write initial test like as of tmpCmdsExample.py in this file ")')
					f.close()

				f = open(ofile, "r", encoding='utf8', errors='ignore'); runcmd=f.read(); f.close()
				exec(runcmd)
		else:
			exec(name);



		print('\n')
	except Exception as e:
		print(e)
		print('\n')
	else:
		pass
	finally:
		pass
