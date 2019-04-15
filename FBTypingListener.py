#import smtplib
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (EMAIL_USER, ", ".join([EMAIL_USER]), "FBSCRIPT - Person is typing", "User " + ID + " is typing on messenger")

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.messenger.com/t/" + ID)

driver.implicitly_wait(10)

login_email = driver.find_element_by_id("email")
login_email.send_keys(FB_USER)

login_pass = driver.find_element_by_id("pass")
login_pass.send_keys(FB_PASS)

driver.find_element_by_id("loginbutton").click()

driver.implicitly_wait(10)

while True:
    print("running")
    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class = '_4a0v _1x3z']"))
        )
        print("Found")
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # server.login(EMAIL_USER, EMAIL_PASS)

        # msg = "FB SCRAPER : Target is typing"
        # server.sendmail(EMAIL_USER, EMAIL_USER, message)
        # server.quit()
        # print("Target is typing!")
        # time.sleep(5)
        toaster.show_toast(driver.find_element_by_id('js_5').find_element_by_tag_name('span').text + " is typing",
                           "Someone is typing in your chat",
                           duration=10)
    except Exception:
        time.sleep(1)
