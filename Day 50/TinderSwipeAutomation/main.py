import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keys as K
import time
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1
})

chrome_path = "" # YOUR CHROME DRIVER PATH
driver = webdriver.Chrome(executable_path=chrome_path, options=opt)
driver.get("https://www.tinder.com")
time.sleep(6)
get_login_button = driver.find_element_by_xpath(
    '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
get_login_button.click()
time.sleep(2)
try:
    fb_button = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]')
except selenium.common.exceptions.NoSuchElementException:
    getmore_button = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/button')
    getmore_button.click()
    time.sleep(1)
    fb_button = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]')
finally:
    fb_button.click()
time.sleep(2)
print(driver.window_handles)
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
get_username_field = driver.find_element_by_id("email")
get_username_field.send_keys(K.USERNAME)
get_password_field = driver.find_element_by_id("pass")
get_password_field.send_keys(K.PASSWORD)
get_password_field.send_keys(Keys.ENTER)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# infobars
location=driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(1)
notification=driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[2]')
notification.click()
time.sleep(3)
while True:
    try:
        like_button=driver.find_element_by_xpath('//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    except selenium.common.exceptions.NoSuchElementException:
        time.sleep(5)
        like_button = driver.find_element_by_xpath(
            '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(3)
        pop_up=driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[2]/button[2]')
        pop_up.click()
        like_button = driver.find_element_by_xpath(
        '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    finally:
        time.sleep(2)
        like_button.click()
