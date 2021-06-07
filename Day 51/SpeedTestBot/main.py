import keys as K
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=K.CHROME_DRIVER_PATH)
        self.down_speed = "NULL"
        self.up_speed = "NULL"

    def get_internet_speed(self):
        self.driver.get(url=K.SPEED_TEST)
        time.sleep(2)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(40)
        try:
            self.down_speed = self.driver.find_element_by_class_name("download-speed").text
            self.up_speed = self.driver.find_element_by_class_name("upload-speed").text
            time.sleep(5)
        except selenium.common.exceptions.NoSuchElementException:
            time.sleep(20)
            self.down_speed = self.driver.find_element_by_class_name("download-speed").text
            self.up_speed = self.driver.find_element_by_class_name("upload-speed").text
            time.sleep(5)

    def tweet_at_provider(self):
        self.driver.get(url=K.TWITTER_URL)
        time.sleep(3)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
        login_button.click()
        time.sleep(3)
        username_box = self.driver.find_element_by_name("session[username_or_email]")
        username_box.send_keys(K.TWITTER_EMAIL)
        password_box = self.driver.find_element_by_name("session[password]")
        password_box.send_keys(K.TWITTER_PASSWROD)
        password_box.send_keys(Keys.ENTER)
        time.sleep(5)
        draft_editor = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
        draft_editor.send_keys(
            f"Hey internet provider, why is my internet speed {self.down_speed}down/{self.up_speed}up when I pay for 100down/100up ?")


Internet_bot = InternetSpeedTwitterBot()
get_speed = Internet_bot.get_internet_speed()
send_tweet = Internet_bot.tweet_at_provider()
