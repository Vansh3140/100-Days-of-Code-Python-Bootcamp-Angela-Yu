from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import time


class InstaFollower:

    def __init__(self, chrome_options):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

    def login(self):
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys("xyz@gmail.com")

        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys("xyz")

        LogIn_btn = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        LogIn_btn.click()
        time.sleep(25)

        save_info = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Save info')]")
        save_info.click()
        time.sleep(20)

        not_now_2 = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        not_now_2.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(5)

        followers = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a")
        followers.click()
        # Scroll till Followers list is there
        pop_up_window = WebDriverWait(
            self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='_aano']")))
        for i in range(5):
            try:
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    pop_up_window)
                time.sleep(2)
            except StaleElementReferenceException:
                # Re-locate the popup window in case it becomes stale
                pop_up_window = WebDriverWait(self.driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='_aano']"))
                )

        self.follow()

        self.driver.quit()

    def follow(self):

        list_followers = self.driver.find_elements(by=By.TAG_NAME, value="button")
        for x in list_followers:
            try:
                x.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(by=By.XPATH,
                                                      value="//button[contains(text(),'Cancel']")
                cancel_btn.click()
