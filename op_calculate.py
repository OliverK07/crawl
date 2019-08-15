# https://www.taifex.com.tw/cht/3/optDailyMarketSummaryExcel
import datetime
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

opcall = "op_call.csv"
opput = "op_put.csv"

# # get all the data
# url = "https://www.taifex.com.tw/cht/3/optDailyMarketSummaryExcel"
# headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# res = requests.get(url, headers=headers)
# data = pd.read_html(res.text)
# for dt in data:
#     print("-----------")
#     print(dt)
# # data[2]: call and data[5]:put is what we need.

# # write to file
# data[2].to_csv(opcall, header=0)
# data[5].to_csv(opput, header=0)

# read from file
call = pd.read_csv(opcall)
call = call.drop(call.index[-2:]) #remove tailing string
call = call.drop([call.columns[0]],axis=1) #remove front column
#remove not this month
print(call)
# put = pd.read_csv(opput)
# print(put)
