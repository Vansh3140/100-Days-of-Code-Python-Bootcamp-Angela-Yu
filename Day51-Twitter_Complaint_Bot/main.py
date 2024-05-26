from selenium import webdriver
from bot import InternetSpeedTwitterBot

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

x_bot = InternetSpeedTwitterBot(chrome_options)
x_bot.get_internet_speed()
x_bot.tweet_at_provider()
