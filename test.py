import requests
from bs4 import BeautifulSoup as bs

# code = '1101'
start_day = '2019/01/15'
end_day = '2019/05/16'

def getRow(code, start_day, end_day):
    url = 'https://www.cnyes.com/twstock/ps_historyprice.aspx?code={0}&ctl00$ContentPlaceHolder1$startText={1}&ctl00$ContentPlaceHolder1$endText={2}'.format(code, start_day, end_day)
    # https://www.cnyes.com/twstock/ps_historyprice.aspx?code=3010&ctl00$ContentPlaceHolder1$startText=2019/01/15&ctl00$ContentPlaceHolder1$endText=2019/05/16
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs(res.text,'html.parser')

    table = soup.findAll('table')
    # print(table)
    # class_="sortcell"
    tds = soup.find_all("td", class_="rt")
    # print("------------------------")
    # print(len(tds))
    if len(tds) > 0:
        end_close=(tds[3].text).replace(',','')
        start_close=(tds[-6].text).replace(',','')
        rang=round((float(end_close)-float(start_close))/float(start_close)*100,2)
        # print(rang)
        return [code, start_close,end_close, str(rang)]
    else:
        return []

import csv
import time
# 開啟 CSV 檔案
tStart = time.time()
with open('trgt.csv', 'w', newline='') as tgt:
    writer = csv.writer(tgt)
    writer.writerow(['No', 'Start', 'End', 'percentage'])
    # writer.writerow(['No', 'Start', 'End'])
    with open('twnumber_orig.csv', newline='') as csvFile:
    # with open('test.csv', newline='') as csvFile:
        rows = csv.reader(csvFile)

        for row in rows:
            if len(row[0]) < 3:
                continue
            print(row[0])
            tmp = getRow(row[0], start_day, end_day)
            writer.writerow(tmp)

tEnd = time.time()
print ("spend time:")
print (tEnd -tStart)
