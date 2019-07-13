import csv
import uuid
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from lxml import html


s1 = "https://finance.yahoo.com/quote/"
s2 = "?p="
columns = defaultdict(list) # each value in each column is appended to a list


with open('data.csv') as f_in , open('data1.csv') as f_out:
    reader = csv.DictReader(f_in) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
    p = columns['symbol']

    fieldnames = reader.fieldnames + ['ADDITIONAL_COLUMN']
    writer_csv = csv.DictWriter(f_out, fieldnames)
    writer_csv.writeheader()


    for row in reader:
        row['ADDITIONAL_COLUMN'] = str(uuid.uuid4().int >> 64) [0:6]
        writer.writerow(row)
    