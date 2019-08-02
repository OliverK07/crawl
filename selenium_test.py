from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

class CompanyData():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\oliver.ke\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
        self.driver.set_window_size(922, 799)
    def __exit__(self):
        self.driver.quit()

    def setUrl(self, url):
        self.url = url
    def setEPSUrl(self):
        self.setUrl("https://www.cnyes.com/twstock/financial4.aspx")
    def setRevUrl(self):
        self.setUrl("https://mops.twse.com.tw/nas/t21/sii/t21sc03_107_4_0.html")

    def getEPS(self):
        self.setEPSUrl()
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_D3").click()
        dropdown = driver.find_element_by_id("ctl00_ContentPlaceHolder1_D3")
        dropdown.find_element_by_xpath("//option[. = '2017Q2']").click()
        driver.implicitly_wait(30)
        tables = pd.read_html(driver.page_source)
        print(tables[0])
        # print(table)
        # driver.quit()

    def getRevenue(self):
        self.setRevUrl()
        driver = self.driver
        driver.get(self.url)
        tables = pd.read_html(driver.page_source)
        for tb in tables:
            print("--------------")
            print(tb)

if __name__ == '__main__':
    tmp = CompanyData()
    # tmp.getEPS()
    tmp.getRevenue()
