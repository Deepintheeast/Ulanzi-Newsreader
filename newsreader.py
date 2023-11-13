from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import requests

# Settingd
ulanzi_url = 'http://192.168.x.x'
max_anzahl_news = 3
cookies_file = 'solaranzeige-cookies.json'
start_url = 'https://solaranzeige.de'
news_url = 'https://solaranzeige.de/phpBB3/search.php?search_id=newposts'

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
#driver.implicitly_wait(60)

# Funktion Daten an Ulanzi senden
def ulanzi_senden(url,data):
    response = requests.post(url, json=data)
# Ende Funktion

# Funktion "Cookies laden"
def load_cookies(driver):
    with open(cookies_file, 'r') as f:
        cookies = json.load(f)
    driver.get(start_url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return driver
# Ende Funktion

# Funktion "Cookies aktualisieren/speichern"
def save_cookies(driver):
    driver.get(start_url)
    #input('Press RETURN to save cookies!')

    cookies = driver.get_cookies()
    cookies = json.dumps(cookies)

    with open(cookies_file, 'w') as f:
        f.write(cookies)
# Ende Funktion

## Programm starten

driver = load_cookies(driver)
time.sleep(3)
seite = driver.get(news_url)
time.sleep(2)
headline = driver.find_elements(By.CLASS_NAME, ('topictitle'))
#time.sleep(3)

i = 0
for value in headline:
    print(value.text)
    i = i + 1
    url = ulanzi_url + '/api/notify'
    data = {
        "text": " Neu !   "+value.text,
        "rtttl": "s:d=4,o=6,b=185:c,p,c,p,c",
        "gradient": [[255,0,0],[0,255,0]],
        "repeat": 1,
        "icon" : "news",
        "pushIcon" : 1,
        "hold": bool(0)
    }
    ulanzi_senden(url, data)

    if i == max_anzahl_news:
        break

save_cookies(driver)
driver.quit()
