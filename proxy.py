from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.webdriver.common.by import By
import pyautogui
import random
from selenium.webdriver.chrome.options import Options
option = Options()
PROXY = input("HTTPProxyを入力してください:") 
option.add_argument('--proxy-server=http://%s' % PROXY)
unicode1=(r'C:\Users\user\OneDrive\デスクトップ\gyazoapi\chromedriver.exe')
browser = webdriver.Chrome(executable_path = unicode1,chrome_options=option)
browser.implicitly_wait(3)
browser.get("http://ipinfo.io/json")
time.sleep(30)
browser.get("https://google.com")
