import datetime
import requests
from bs4 import BeautifulSoup as bs
import csv
import time

class crawl():
    def __init__(self,name):
        self.name = name
        
    def getDate(self, inputDate):
        # inputDate = input("Enter date in format 'yyyy/mm/dd' :")
        year,month,day = inputDate.split('/')
        isValidDate=True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False
        if(isValidDate == False):
            print("Input date invalid")
            return "2010/01/01"
        else:
            return "{0}/{1:02d}/{2:02d}".format(int(year),int(month),int(day))

# TODO: use decorate
    def setStartDate(self, inputDate):
        # print("Set start date:")
        self.startDate = self.getDate(inputDate)
    def getStartdate(self):
        return self.startDate

# TODO: use decorate
    def setEndDate(self, inputDate):
        # print("Set End date:")
        self.endDate = self.getDate(inputDate)
    def getEnddate(self):
        return self.endDate

    def setCode(self, code):
        self.code = code

    def createURL(self):
        self.url = 'https://www.cnyes.com/twstock/ps_historyprice.aspx?code={0}&ctl00$ContentPlaceHolder1$startText={1}&ctl00$ContentPlaceHolder1$endText={2}'.format(self.code, self.startDate, self.endDate)
    def getRow(self):
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        res = requests.get(self.url, headers=headers)
        soup = bs(res.text,'html.parser')

        table = soup.findAll('table')
        tds = soup.find_all("td", class_="rt")
        if len(tds) > 0:
            # TODO: fix this for more flexible
            end_close=(tds[3].text).replace(',','')
            start_close=(tds[-6].text).replace(',','')
            rang=round((float(end_close)-float(start_close))/float(start_close)*100,2)
            return [self.code, start_close,end_close, str(rang)]
        else:
            return []


if __name__ == '__main__':
    tStart = time.time()
    sourceFile = input("Enter Source csv name:")
    targetFile = input("Enter Target csv name:")
    s_Date = input("Enter Start date in format 'yyyy/mm/dd' :")
    e_Date = input("Enter End date in format 'yyyy/mm/dd' :")
    with open(targetFile, 'w', newline='') as tgt:
        writer = csv.writer(tgt)
        writer.writerow(['No', 'Start', 'End', 'percentage'])
        # writer.writerow(['No', 'Start', 'End'])
        with open(sourceFile, newline='') as csvFile:
            tmp = crawl("tmp")
            # with open('test.csv', newline='') as csvFile:
            rows = csv.reader(csvFile)
            for row in rows:
                if len(row[0]) < 3:
                    print("Source file content invalid.")
                    continue
                print("Dealing code: " +row[0])
                # tmp = getRow(row[0], start_day, end_day)
                tmp.setCode(row[0])
                tmp.setStartDate(s_Date)
                tmp.setEndDate(e_Date)
                tmp.createURL()
                writer.writerow(tmp.getRow())

    tEnd = time.time()
    print ("spend time:")
    print (tEnd -tStart)

