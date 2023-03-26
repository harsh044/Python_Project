from selenium import webdriver
import pyttsx3 as p
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def wiki(query):
    query = query
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    driver.get(url="https://www.wikipedia.org")
    search = driver.find_element_by_xpath('//*[@id="searchInput"]')
    search.click()
    search.send_keys(query)

    enter = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
    enter.click()

    info = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]')
    text = info.text
    engine=p.init()
    engine.say(text)
    engine.runAndWait()
