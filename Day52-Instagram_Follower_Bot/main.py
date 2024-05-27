from selenium import webdriver
from selenium.webdriver.common.by import By
from follower import InstaFollower

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot_followers = InstaFollower(chrome_options)
bot_followers.login()
bot_followers.find_followers()
