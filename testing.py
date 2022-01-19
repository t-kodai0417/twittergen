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
#vpn
print('15秒以内にvpnに接続しなさい。')
time.sleep(15)
#mail connect
kukuru="https://m.kuku.lu"
browser.get(kukuru)
time.sleep(3)
#期限付きのメルアドを取得
kigen = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div[6]/div[1]/div[5]/a")
kigen.click()
time.sleep(5)
#メルアドを取得
getma = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div/div/div/div/div[1]/u/b")
print(getma.text)
sutema=getma.text
time.sleep(1)
#メルアドをコピー
copymail=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div/div/div/div/div[4]/a")
copymail.click()
#タブを追加してそっちにいく
browser.execute_script("window.open()")
browser.switch_to.window(browser.window_handles[1])
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
mail_input="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/label/div/div[2]/div/input"
tw_mail = browser.find_element(by=By.XPATH, value=mail_input)
tw_mail.click()
pyautogui.keyDown('ctrl')
pyautogui.press(['v'])
pyautogui.keyUp('ctrl')
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
#clickbutton
divbutton1 = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
divbutton1.click()
time.sleep(1)

divbutton2 = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
divbutton2.click()
divbutton3 = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div")
time.sleep(1)
divbutton3.click()
#--------------------------------
#devmode
browser.switch_to.window(browser.window_handles[0])
#dev1--メールアドレスを選択する
dev1 = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div[8]/div[4]/div/div[1]/div[2]/div[1]/a")
dev1.click()
#dev2--受信トレイを開く
dev2 = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[25]/div/div/div[4]/div[3]/a")
dev2.click()
#dev3--メールの件名を取得する
browser.refresh()
time.sleep(4)
browser.refresh()
time.sleep(3)
#再読み込み→get
dev3 = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div/div[6]/div/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/a/div[1]/b/span")
print(dev3.text)
aaaa=dev3.text
aa22=aaaa.replace('Twitterの認証コードは', '')
s=aa22.replace('です', '')
print(s)
browser.switch_to.window(browser.window_handles[1])
vericode=browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input")
vericode.clear()
vericode.send_keys(s)
#dev4--verify
dev4 = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
dev4.click()
#dev5--パスワードを入力
dev5=browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div[1]/input")
dev5.clear()
dev5_pass="kodai0417@"
dev5.send_keys(dev5_pass)
time.sleep(2)
#dev6--次へ
#class=css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1tl8opc r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0
#span=/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/span
dev6=browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div")
dev6.click()
#dev7--アイコンをbypass
dev7=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
dev7.click()
#dev8--自己紹介をbypass
dev8=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
dev8.click()
#dev9--UserIdをbypass
dev9=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
dev9.click()
#dev10--Twitterメインページへ逃亡
browser.get("https://twitter.com")
#-------------------------
print('多分完了しました。')
print(f"メルアド:{sutema}")
print("パスワード:kodai0417@")
time.sleep(15)
