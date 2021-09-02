from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pyttsx3 as p
class youtube():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path="C:\selenium\msedgedriver.exe")

    def video(self,query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/")
        # search=WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="search"]'))).click()
        search = self.driver.find_element_by_xpath('//*[@id="search"]')
        search.click()
        search.send_keys(query+Keys.ENTER)

        WebDriverWait(self.driver,70).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="video-title"]/yt-formatted-string'))).click()
        WebDriverWait(self.driver, 70).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[2]/button[8]'))).click()
        # enter = self.driver.find_element_by_xpath('//*[@id="movie_player"]/div[27]/div[2]/div[2]/button[8]')
        # enter.click()

        # video = self.driver.find_element_by_id("img")
        # video.click()

# bot = youtube()
# bot.video("hirkani full movie")