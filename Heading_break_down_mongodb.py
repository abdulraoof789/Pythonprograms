from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pdb
import bs4
import requests
import time
import itertools
import json
import csv
import pymongo
from pymongo import MongoClient
import pandas as pd
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["IndiaLaw"]
mycol = mydb["IndiaLawdata"]
x = mycol.find()
csv_file = open('testing_Heading.csv','a')
writer = csv.writer(csv_file)
data_1_1 = []
for data in x:
    data_1_number = (data['Heading'].split(' '))
    #print(data_1_number[0])
    data_1_date = (data['Heading'].split())
    data_1_date_2 = (data_1_date[1:])
    #data_1_1.append(data_1_date_2[-1])
    #print(len(data_1_1))
    #print(data_1_number[0] + data_1_date_2[-1])
    data_1_appelvsrespon = (data['Heading'].split())
    data_1_appelvsrespon_1 = [x.split('[') for x in data_1_appelvsrespon]
    data_1_appelvsrespon_2 = (data_1_appelvsrespon[1:-1])
    data_1_appelvsrespon_2 = ' '.join(data_1_appelvsrespon_2)
    data_1_appelvsrespon_3 = (data_1_appelvsrespon_2.split('['))
    if 'vs.' in (data_1_appelvsrespon_3[0]):
       data_1_appelvsrespon_4 = data_1_appelvsrespon_3[0].split('vs.')
       Appelent = data_1_appelvsrespon_4[0]
       Respondent = data_1_appelvsrespon_4[1]
       #print(Appelent + Respondent)
    else:
       data_1_appelvsrespon_5 = data_1_appelvsrespon_3[0]
       print(data_1_appelvsrespon_5)
       #writer.writerow(yes_1 + data_1)
       #Appelent_1 = data_1_appelvsrespon_5
       #print(Appelent_1)
       #Respondent = data_1_appelvsrespon_5[1]
       #print(Appelent)
