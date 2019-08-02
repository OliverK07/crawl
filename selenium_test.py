from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox(executable_path=r'C:\Users\oliver.ke\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("https://www.cnyes.com/twstock/financial4.aspx")
driver.set_window_size(922, 799)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_D3").click()
dropdown = driver.find_element_by_id("ctl00_ContentPlaceHolder1_D3")
dropdown.find_element_by_xpath("//option[. = '2017Q2']").click()
driver.implicitly_wait(30)
# soup = bs(driver.page_source,'html.parser')
# import requests
# url = "https://www.cnyes.com/twstock/financial4.aspx"
# headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# res = requests.get(url, headers=headers)
# soup = bs(res.text,'html.parser')
# table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView1'})
import pandas as pd
tables = pd.read_html(driver.page_source)
for tb in tables:
    print("-----------------")
    print(tb)
# print(table)
driver.quit()
