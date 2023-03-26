from selenium import webdriver
import pyttsx3 as p
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def news(self,query):
    query = query
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    driver.get(url="https://news.google.com")
    search = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    search.click()
    search.send_keys(query)

    enter = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/button[4]')
    enter.click()
