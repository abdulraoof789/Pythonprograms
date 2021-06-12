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
from openpyxl import Workbook
from pymongo import MongoClient
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from itertools import groupby
import xlsxwriter
import pandas as pd
book = Workbook()
sheet = book.active
separator = ','
csv_file = open('court.csv','r')
reader = csv.reader(csv_file)
data = []
for i in reader:
    data.append(i)
flattened = [val for sublist in data for val in sublist]
for elem in flattened:
    print(elem)
    driver = webdriver.Firefox(executable_path = './geckodriver')
    url = ('http://www.indialawlibrary.com/AdvanceSearch.aspx')
    driver.get(url)
    time.sleep(10)
    court = driver.find_element_by_id('ContentPlaceHolder1_lstCourt')
    court.send_keys(elem)
    time.sleep(5)
    button = driver.find_element_by_id('ContentPlaceHolder1_cmdSearch').click()
    time.sleep(10)
    for page in range(30950,82940,10):
        next = driver.current_url[:53]+str(page)
        driver.get(next)
        para = driver.find_elements_by_tag_name('p')
        for elem in para:
            a = (elem.text.splitlines())
            if len(a)>0:
               print(a)
               csv_file = open('Bombay_court_paragragh_1.csv','a')
               writer = csv.writer(csv_file)
               writer.writerow(a)
               #sheet.append(a)
               #book.save('Bombay_court_paragragh_1.xlsx')
    	
