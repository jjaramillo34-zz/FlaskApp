import csv
import uuid
import requests
import os
from bs4 import BeautifulSoup
from collections import defaultdict
from lxml import html

#remove files
os.remove("data1.csv")
os.remove("yahoo.html")
#create files
open('data1.csv', "a")
open('yahoo.html', "a")

columns = defaultdict(list) # each value in each column is appended to a list
s1 = "https://finance.yahoo.com/quote/"
s2 = "?p="
s3 = "&.tsrc=fin-srch"
data = []

with open('data.csv', 'r') as fin, open('data1.csv', 'w') as fout, open('yahoo.html', 'w') as htmlfile:
    reader = csv.reader(fin, delimiter=',')
    writer = csv.writer(fout, delimiter=',')
    # set headers here, grabbing headers from reader first
    writer.writerow(next(reader) + ['YahooLink'] + ['YahooData1'] + ['YahooData2'])
    i = 0
    for row in reader:
        data.append(row[7])
        #print(row[7])
        print(len(data) + 1)
        if data[i] != "":
            page1 = s1 + data[i] + s2 + data[i] + s3
            page = requests.get(page1)
            tree = html.fromstring(page.content)
            htmlfile.write(str(page.content))
            #print(page.content)
            stock1 = tree.xpath('//*[@id="quote-header-info"]/div[3]/div/span/text()')
            stock2 = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()')        
            new_value1 = stock1
            new_value2 = stock2
            #print(new_value1)
            #print(new_value2)
            row.append(page1)
            row.append(new_value1)
            row.append(new_value2)
            writer.writerow(row)
        else:
            print('Symbol Empty....')
        i += 1
        
    #close files   
    fin.close()
    fout.close()
    htmlfile.close()               