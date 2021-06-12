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
    for elem1 in range(0,83180,10):
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
               csv_file_1 = open('India_law_data.csv','a')
               writer = csv.writer(csv_file_1)
               writer.writerow(para_1 + data1)
               
               
            if len(para_1) == 3:
               para_4 = []
               para_3 = (para_1[1] + para_1[2])
               para_4.append(para_3)
               csv_file_1 = open('India_law_data.csv','a')
               writer = csv.writer(csv_file_1)
               para_2 = []
               para_2.append(para_1[0])
               writer.writerow(para_2 + para_4 + data1)
               
               
            
            url1 = ('http://www.indialawlibrary.com/ResultPage.aspx?start=%s' %elem1)
            driver.get(url1)
