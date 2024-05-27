from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Beautiful-Soup Web Scraping Part

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

temp_links = soup.find_all(name="a", class_="property-card-link")
temp_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
temp_addresses = soup.find_all(name="address")

house_links = []
for x in temp_links:
    house_links.append(x.get("href"))

house_prices = []
for x in temp_prices:
    house_prices.append(x.get_text().replace("/mo", "").replace("+",""))


house_addresses = []
for x in temp_addresses:
    house_addresses.append(x.get_text().replace("\n", "").replace("|", "").strip())

# Selenium Part

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

for x in range(len(house_links)):
    time.sleep(10)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSecXHwLXl5VZ_t34VJWCbHDQ94fzYU22zqXQPH9pOqvYpsylA/viewform")
    time.sleep(5)

    input_list = driver.find_elements(by=By.XPATH, value="//input[@type='text']")

    input_list[0].send_keys(house_addresses[x])
    input_list[1].send_keys(house_prices[x])
    input_list[2].send_keys(house_links[x])

    submit = driver.find_element(by=By.XPATH, value="//span[text()='Submit']")
    submit.click()

