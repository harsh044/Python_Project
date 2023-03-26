from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pyttsx3 as p
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def video(query):
    query = query
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # driver = webdriver.Chrome(executable_path="C:/selenium/chromedriver.exe")
    # driver = webdriver.Firefox(executable_path="C:/selenium/geckodriver.exe")
    # driver = webdriver.Edge(executable_path="C:/selenium/msedgedriver.exe")
    driver.get(url="https://www.youtube.com/")
    driver.implicitly_wait(10)
    search = driver.find_element(By.XPATH,'//input[@id="search"]')
    
    search.click()
    search.send_keys(query+Keys.ENTER)

    WebDriverWait(driver,70).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="video-title"]/yt-formatted-string'))).click()
    WebDriverWait(driver, 70).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[2]/button[8]'))).click()
