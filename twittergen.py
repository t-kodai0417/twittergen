from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
import pyautogui
import random
unicode1=(r'C:\Users\user\OneDrive\デスクトップ\gyazoapi\chromedriver.exe')
browser = webdriver.Chrome(executable_path = unicode1)
browser.implicitly_wait(3)
print('15秒以内にvpnに接続しなさい。')
time.sleep(15)
url_login = 'https://twitter.com/i/flow/signup'
print(f"Access{url_login}")
browser.get(url_login)
time.sleep(10)
print("SuccessfullyAccessed")
twuser="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
print('15秒以内にrecaptcha認証を完了させなさい。')
time.sleep(15)
browser_from = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/form/div[2]/div[2]/button")
browser_from.click()
print("The button is pushed!")
links = browser.find_element(by=By.XPATH, value="/html/body/div/div[3]/div[2]/div[2]/input")
links.click()
pyautogui.keyDown('ctrl')
pyautogui.press(['c'])
pyautogui.keyUp('ctrl')
time.sleep(1)
browser.get("https://discord.com/register")
links = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input")
links.click()
pyautogui.keyDown('ctrl')
pyautogui.press(['v'])
pyautogui.keyUp('ctrl')
#print(random.randint(1000, 9999))
random1=(random.randint(1000, 9999))
USER=(f"Tinker{random1}")
element=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input")
element.clear()
element.send_keys(USER)
password="kodai0417"
element=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input")
element.clear()
element.send_keys(password)
year=("2000")
element=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/input")
element.clear()
element.send_keys(year)
month=("1")
element=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/input")
element.clear()
element.send_keys(month)
days=("11")
element=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[3]/div/div/div/div/div[1]/div[2]/div/input")
element.clear()
element.send_keys(days)
links = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div/form/div/div/div[5]/button")
links.click()
print('認証しなさい。')
time.sleep(30)
