from selenium import webdriver
import pyttsx3 as p
class info():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path="C:\selenium\msedgedriver.exe")

    def wiki(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()

        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]')
        text = info.text
        engine=p.init()
        engine.say(text)
        engine.runAndWait()

# bot = info()
# bot.wiki("Harry Potter")