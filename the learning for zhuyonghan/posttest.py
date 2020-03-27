#coding=utf-8
import requests
import json
import sys
import time
#import xlrd
'''
dataexcel = xlrd.open_workbook('emailclose3mouth.xlsx')
table = dataexcel.sheets()[0]
nrows = table.nrows
'''
url =  "https://api.exmail.qq.com/cgi-bin/log/operation?access_token=gtV7DiSnJyZ0YR34ZbgWZLqH1JAkhVHlOa5CE9VnDHAxr9sJiEA1s_WN38tvgZ6R_u_u14QxO4ct52dH9KQyRw"
url2 = "https://api.exmail.qq.com/cgi-bin/log/mailstatus?access_token=gtV7DiSnJyZ0YR34ZbgWZLqH1JAkhVHlOa5CE9VnDHAxr9sJiEA1s_WN38tvgZ6R_u_u14QxO4ct52dH9KQyRw"
'''
for i in range(nrows):

    print(table.row_values(i)[0])
    if i >5:
        exit()
'''

#for i in listemail:
adata = {"type": 0,	"begin_date": "2020-03-01",	"end_date": "2020-03-25"}
adata2 ={"domain": "wyn88.com",	"begin_date": "2020-03-19",	"end_date": "2020-03-19"}
#每企业调用单个cgi/api不可超过500次/分，15000次/小时 企业每ip调用接口不可超过10000次/分，300000次/小时
time.sleep(0.1)
response = requests.post(url2, data=json.dumps(adata2))

print (response.text)


