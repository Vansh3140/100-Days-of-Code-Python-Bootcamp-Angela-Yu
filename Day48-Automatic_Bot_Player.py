from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

initial_time = time.time()
timeout = 300

powers = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]

while time.time() < initial_time + timeout:
    cookie = driver.find_element(by=By.ID, value="cookie")
    temp_time = time.time() + 5
    while time.time() < temp_time:
        cookie.click()
    cookie_count = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))

    for x in range(7, -1, -1):
        temp_str = "buy" + powers[x]
        try:
            temp_cost = driver.find_element(by=By.CSS_SELECTOR, value=f"[id='{temp_str}'] b").text.split()
            temp_val = int(temp_cost[-1].replace(",", ""))
            while cookie_count >= temp_val:
                temp_click = driver.find_element(by=By.CSS_SELECTOR, value=f"[id='{temp_str}']")
                temp_click.click()
                cookie_count = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))
                temp_cost = driver.find_element(by=By.CSS_SELECTOR, value=f"[id='{temp_str}'] b").text.split()
                temp_val = int(temp_cost[-1].replace(",", ""))
        except StaleElementReferenceException:
            # Re-fetch the element if it becomes stale
            temp_cost = driver.find_element(by=By.CSS_SELECTOR, value=f"[id='{temp_str}'] b").text.split()
            temp_val = int(temp_cost[-1].replace(",", ""))
            continue

print(driver.find_element(by=By.ID, value="cps").text)
driver.quit()
