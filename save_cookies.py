from selenium import webdriver
import json

cookies_file = 'solaranzeige-cookies.json'
start_url = 'https://solaranzeige.de'
driver = webdriver.Firefox()


def save_cookies(driver):
    driver.get(start_url)
    input('Press RETURN to save cookies!')

    cookies = driver.get_cookies()
    cookies = json.dumps(cookies)

    with open(cookies_file, 'w') as f:
        f.write(cookies)

    driver.quit()


def load_cookies(driver):
    with open(cookies_file, 'r') as f:
        cookies = json.load(f)

    driver.get(start_url)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    return driver


save_cookies(driver)
#driver = load_cookies(driver)
