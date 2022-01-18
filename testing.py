from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.webdriver.common.by import By
import pyautogui
import random
unicode1=(r'C:\Users\user\OneDrive\デスクトップ\gyazoapi\chromedriver.exe')
browser = webdriver.Chrome(executable_path = unicode1)
browser.implicitly_wait(3)
#twitterに接続
url_login = 'https://twitter.com/i/flow/signup'
print(f"Access:{url_login}")
browser.get(url_login)
time.sleep(5)
print("SuccessfullyAccessed")
#twuser is twitter user.
#user名を入力
tw_user="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
twuser=browser.find_element(by=By.XPATH, value=tw_user)
twuser.clear()
random1=(random.randint(1000, 9999))
USER=(f"Tinker{random1}")
twuser.send_keys(USER)
#電話番号→メール
changemail = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/span")
changemail.click()
#メルアド入力
mail=aaa@aaa.aaa
mail_input="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/label/div/div[2]/div/input"
tw_mail = browser.find_element(by=By.XPATH, value=mail_input)
tw_mail.send_keys(mail)
#誕生日等を入力
#月
select_element = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/div[3]/div/div[1]/select")
select_object = Select(select_element)
select_object.select_by_index(1)
#日
select_element = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/div[3]/div/div[2]/select")
select_object = Select(select_element)
select_object.select_by_index(5)
#年
select_element = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/div[3]/div/div[3]/select")
select_object = Select(select_element)
select_object.select_by_index(25)
#--------------------------------
time.sleep(30)
