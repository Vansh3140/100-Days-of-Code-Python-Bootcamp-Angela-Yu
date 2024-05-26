from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.zoosk.com/")

time.sleep(5)

accept_cookies = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
accept_cookies.click()

time.sleep(5)

# Login Button Press
login_btn = driver.find_element(by=By.CLASS_NAME, value="zoosk-header-responsive-aes__login-link")
login_btn.click()

# Entering Username and Password

username = driver.find_element(by=By.ID, value="login-email")
username.send_keys("workman3140@gmail.com")

password = driver.find_element(by=By.ID, value="login-password")
password.send_keys("Vansh@123")

# Filling Captcha
time.sleep(25)

login_click_btn = driver.find_element(by=By.XPATH,
                                      value="/html/body/touch-root/div/div[1]/app-login/main/div/login-email/div/div/div/div/login-form/form/div[5]/button")
login_click_btn.click()

initial_time = time.time()
time.sleep(10)

global x
x = 0

while time.time() < initial_time + 600:
    time.sleep(4)
    try:
        right_swipe = driver.find_element(by=By.ID, value="search-yes-button")
        right_swipe.click()
        time.sleep(4)
        move_next = driver.find_element(by=By.ID, value=f"slide-next-button{x}")
        move_next.click()
        print("1")
    except:
        move_next = driver.find_element(by=By.ID, value=f"slide-next-button{x}")
        move_next.click()
        print("2")
    x += 1

driver.quit()
