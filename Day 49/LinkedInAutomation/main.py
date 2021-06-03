from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys as K

driver = webdriver.Chrome(executable_path=K.chrome_driver_path)
driver.get(url=K.linkedIn_login_page)
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys(K.username)
password.send_keys(K.password)
password.send_keys(Keys.ENTER)
time.sleep(2)
# logged in

driver.get(url=K.job_search_url)
time.sleep(2)
# job search page
apply_button = driver.find_element_by_class_name("jobs-apply-button")
apply_button.click()
time.sleep(2)
# apply button
next_button=driver.find_element_by_xpath('//*[@id="ember310"]/span')
next_button.click()
next_button.click()
# final procedures