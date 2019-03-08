from selenium import webdriver
import json
from time import sleep
from re import findall


def find_input_login(*args):
    for i in args:
        browser.find_element_by_css_selector(i).click()
    # browser.find_element_by_id("react-tabs-0").click()


def login_input(input_username, input_password, username, password):
    browser.find_element_by_id(input_username).clear()
    browser.find_element_by_id(input_password).clear()
    browser.find_element_by_id(input_username).send_keys(username)
    browser.find_element_by_id(input_password).send_keys(password)


def login(button_login, verify):
    if verify == True:
        captcha("recaptcha-checkbox-checkmark")
    browser.find_element_by_id(button_login).click()


def captcha(input_captcha):
    # browser.find_element_by_class_name("recaptcha-checkbox-checkmark").click()
    pass


def save_cookie(filename='domain', localStorage=False):
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    with open(filename+'.cookie', 'w') as f:
        f.write(jsonCookies)
    if localStorage == True:
        token = browser.execute_script("return localStorage.getItem('jwt')")
        return(token)


def set_cookie(filename='domain', listCookies=[], localStorage=False, token=[]):
    browser.delete_all_cookies()
    for cookie in listCookies:
        # for (b, v) in cookie.items():
        #     browser.add_cookie({b: v})
        browser.add_cookie({
            'domain': cookie['domain'],
            'name': cookie['name'],
            'value': cookie['value'],
            'path': cookie['path'],
            'httpOnly': cookie['httpOnly'],
            'secure': cookie['secure']
        })

    if localStorage == True:
        browser.execute_script("localStorage.setItem(%s)" % token)


def checkin(button_checkin):
    browser.find_element_by_id(button_checkin).click()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://127.0.0.1:1080")
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # disable image
browser = webdriver.Chrome(chrome_options=chromeOptions, executable_path="chromedriver.exe")
username = "mixterjim"
password = "password"
website = "http://mixterjim.github.io/"  # chrono.gg
token = "'jwt','abcdefghijklmnopqrstuvwxyz'"

filename = findall(r"(?<=\.)\w*(?=\.\w*\/)\w*(?=\.\w*\/)", website)[0]  # get domain name
browser.get(website)
now_handle = browser.current_window_handle
browser.switch_to_window(now_handle)
try:
    f = open(filename+'.cookie', 'r', encoding='utf-8')
    listCookies = json.loads(f.read())
    set_cookie(filename, listCookies, token=token, localStorage=1)
    browser.get(website)
except IOError:
    find_input_login(".register", ".modal-tab")
    login_input("signin-email", "signin-password", username, password)
    # login("signin", 0)

sleep(3)
checkin("reward-coin")
save_cookie(filename)
if browser.find_element_by_id("reward-coin").get_attribute("class") == "coin dead":
    print("Done")
    browser.quit()
