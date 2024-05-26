from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = "xyz@gmail.com"
TWITTER_PASSWORD = "xyz"


class InternetSpeedTwitterBot:

    def __init__(self, chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        go_btn = self.driver.find_element(by=By.XPATH,
                                          value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_btn.click()
        time.sleep(120)

        up_speed = self.driver.find_elements(by=By.CLASS_NAME, value="result-data-large")
        self.up = up_speed[0].text
        self.down = up_speed[1].text
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        time.sleep(10)

        cross_mark = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div[2]/div/div/div/button")
        cross_mark.click()
        first_sign_in = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div/span/span")
        first_sign_in.click()
        time.sleep(10)

        email_id = self.driver.find_element(by=By.NAME, value="text")
        email_id.send_keys(TWITTER_EMAIL)
        next_btn = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span")
        next_btn.click()
        time.sleep(10)

        email_id_password = self.driver.find_element(by=By.NAME, value="password")
        email_id_password.send_keys(TWITTER_PASSWORD)
        log_in_btn = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span")
        log_in_btn.click()
        time.sleep(10)

        post_x = self.driver.find_element(by=By.LINK_TEXT, value="Post")
        post_x.click()
        time.sleep(10)

        post_content = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        post_content.send_keys(f"Hey @JioCare ,why is my internet speed {self.down}down/{self.up}up when i pay for 10down/30up")
        post_final_btn = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span")
        post_final_btn.click()
        self.driver.quit()




