from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3 as p
class questions():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path="C:\selenium\msedgedriver.exe")

    def question(self,query):
        self.query = query
        self.driver.get(url="https://www.answers.com/")
        search = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/form/div/div/div/div/input')
        search.click()
        search.send_keys(query + Keys.ENTER)

        enter = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[3]/div')
        enter.click()

        ans = self.driver.find_element_by_xpath('//*[@id="answer_58555"]/div[3]/div/p')
        text1= ans.text
        engine = p.init()
        engine.say(text1)
        engine.runAndWait()

        # enter = self.driver.find_element_by_id("img")
        # enter.click()

        # info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[3]/ul/li[1]')
        # text = info.text
        # engine=p.init()
        # engine.say(text)
        # engine.runAndWait()

# bot = questions()
# bot.question("What is Internet?")