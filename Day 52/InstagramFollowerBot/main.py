import time

import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys

import keys as K
from selenium import webdriver


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=K.CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(f"https://www.instagram.com/accounts/{K.SIMILAR_ACCOUNT}")
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(K.USERNAME)
        passs = self.driver.find_element_by_name("password")
        passs.send_keys(K.PASSWORD)
        passs.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/instagram/")
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        for i in range(2):
            div = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div)
            time.sleep(2)

    def follow(self):
        all_buttons=self.driver.find_elements_by_css_selector('li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except selenium.common.exceptions.ElementClickInterceptedException:
                print("Error")
                time.sleep(5)



instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
instafollower.follow()
