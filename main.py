from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"PATH\chromedriver.exe"
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"
service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self, driver_path, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go_button.click()
        time.sleep(45)
        close_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/'
                                                                   'div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        close_button.click()
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                                '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                                '/div[1]/div/div[2]/span').text
        time.sleep(1)
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                              '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                              '/div[2]/div/div[2]/span').text
        time.sleep(1)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        self.email = self.driver.find_element(by=By.NAME, value="text")
        self.email.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                                  'div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(1)
        username = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                               'div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/'
                                                               'label/div/div[2]/div/input')
        username.send_keys("USERNAME")
        time.sleep(1)
        next_button_two = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/'
                                                                      'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/'
                                                                      'div/div/div/div/div')
        next_button_two.click()
        time.sleep(1)
        self.password = self.driver.find_element(by=By.NAME, value="password")
        self.password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        log_in_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                                    'div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/'
                                                                    'div/div/div/div')
        log_in_button.click()
        time.sleep(5)
        twitter_post = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                   'div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/'
                                                                   'div/div/div[2]/div[1]/div/div/div/div/div/div/div/'
                                                                   'div/div/div/label/div[1]/div/div/div/div/div/'
                                                                   'div[2]/div/div/div/div')
        twitter_post.click()
        time.sleep(2)
        twitter_private = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                      'div/div/div[1]/div/div[3]/div/div[2]/div[1]/'
                                                                      'div/div/div/div[2]/div[1]/div/div/div/div/div/'
                                                                      'div[1]/div/div')
        twitter_private.click()
        time.sleep(2)
        twitter_circle = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div[2]/div/'
                                                                     'div[2]/div/div/div/div/div/div/div[3]')
        twitter_circle.click()
        time.sleep(2)
        twitter_post = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                   'div/div/div/div/div[3]/div/div[2]/div[1]/div/div/'
                                                                   'div/div[2]/div[1]/div/div/div/div/div/div[2]/div/'
                                                                   'div/div/div/label/div[1]/div/div/div/div/div/'
                                                                   'div[2]/div/div/div/div')
        twitter_post.send_keys(f"Testing Python Download{self.down}Mbps, Upload{self.up}Mbps")
        time.sleep(2)
        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                   'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                                   'div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/'
                                                                   'span/span')
        tweet_button.click()
        time.sleep(1000)

bot = InternetSpeedTwitterBot(service, TWITTER_EMAIL, TWITTER_PASSWORD)
bot.get_internet_speed()
bot.tweet_at_provider()
