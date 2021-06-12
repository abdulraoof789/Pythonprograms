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
mycol_1 = mydb["IndiaLawdata_5000"]
x = mycol.find()
csv_file = open('judgement_5000.csv','a')
writer = csv.writer(csv_file)
for data in x:
    data_Heading_1 = []
    data_Heading = (data['Heading'])
    data_Heading_1.append(data_Heading)
    print(data_Heading_1)
    data_Paragraph_1 = []
    data_Paragraph = (data['Paragraph'])
    data_Paragraph_1.append(data_Paragraph)
    print(data_Paragraph_1)
    data_Judgement_1 = []
    data_Judgement = (data['Judgement'])
    data_Judgement_1.append(data_Judgement[:5000])
    print(data_Judgement_1)
    writer.writerow(data_Heading_1+data_Paragraph_1+data_Judgement_1)
    mydict1 = { "Heading":data_Heading, "Paragraph":data_Paragraph ,"Judgement": data_Judgement[:5000]}
    insert = mycol_1.insert_one(mydict1)
