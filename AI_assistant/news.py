from selenium import webdriver
import pyttsx3 as p
class newspage():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path="C:\selenium\msedgedriver.exe")

    def news(self,query):
        self.query = query
        self.driver.get(url="https://news.google.com")
        search = self.driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/button[4]')
        enter.click()

# bot = newspage()
# bot.news("tech")