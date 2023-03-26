from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3 as p
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def question(query):
    query = query
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    driver.get(url="https://www.answers.com/")
    search = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/form/div/div/div/div/input')
    search.click()
    search.send_keys(query + Keys.ENTER)

    enter = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[3]/div')
    enter.click()

    ans = driver.find_element_by_xpath('//*[@id="answer_58555"]/div[3]/div/p')
    text1= ans.text
    engine = p.init()
    engine.say(text1)
    engine.runAndWait()
