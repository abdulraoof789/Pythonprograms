from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pdb
import bs4
import requests
import time
import itertools
import json
from openpyxl import Workbook
import csv
import pymongo
from pymongo import MongoClient
import pandas as pd
book = Workbook()
sheet = book.active
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["IndiaLaw"]
mycol = mydb["IndiaLawdata"]
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from itertools import groupby
separator = ','
driver = webdriver.Firefox(executable_path = './geckodriver')
csv_file = open('court.csv','r')
reader = csv.reader(csv_file)
data = []
for i in reader:
    data.append(i)
flattened = [val for sublist in data for val in sublist]
for elem2 in flattened:
    url = ('http://www.indialawlibrary.com/AdvanceSearch.aspx')
    driver.get(url)
    time.sleep(5)
    court = driver.find_element_by_id('ContentPlaceHolder1_lstCourt')
    court.send_keys(elem2)
    time.sleep(5)
    button = driver.find_element_by_id('ContentPlaceHolder1_cmdSearch').click()
    time.sleep(5)
    for elem1 in range(39090,40000,10):
        url = ('http://www.indialawlibrary.com/ResultPage.aspx?start=%s' %elem1)
        driver.get(url)
        for i in range(0,10):
            para_graph = driver.find_elements_by_id('lnkresult')[i].text
            para = driver.find_elements_by_id('lnkresult')[i].click()
            data_2 = []
            time.sleep(5)
            para2 = driver.find_elements_by_tag_name('p')
            data = []
            for elem in para2:
                data.append(elem.text)
            data1 = []
            i3 = (separator.join(data))
            data1.append(i3)
            para_1 = (para_graph.splitlines())
            if len(para_1) == 2:
               mydict = { "Heading": para_1[0], "Paragraph": para_1[1],"Judgement": i3}
               insert = mycol.insert_one(mydict)
               
            if len(para_1) == 3:
               para_3 = (para_1[1] + para_1[2])
               mydict1 = { "Heading": para_1[0], "Paragraph": para_3,"Judgement": i3}
               insert = mycol.insert_one(mydict1)
               
            
            url1 = ('http://www.indialawlibrary.com/ResultPage.aspx?start=%s' %elem1)
            driver.get(url1)
