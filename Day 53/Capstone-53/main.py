import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import keys as K

# get the zillow web page
res = requests.get(url=K.ZILLOW_LINK, headers=K.ZILLOW_HEADER)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
get_items = soup.select(".list-card-top a")
links = []  # all the links
for x in get_items:
    href = x["href"]
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

# all the address
get_address=soup.select(".list-card-info address")
address=[add.get_text().split(" | ")[-1] for add in get_address]

# all the price
get_prices=soup.select(".list-card-heading div")
prices=[price.get_text() for price in get_prices]

# Filling the google forms
driver=webdriver.Chrome(executable_path=K.CHROME_DRIVER_PATH)
for n in range(len(links)):
    driver.get(url=K.FORM_LINK)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address[n])
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[n])
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[n])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
