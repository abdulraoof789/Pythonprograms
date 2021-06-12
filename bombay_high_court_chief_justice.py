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
import sys
from pymongo import MongoClient
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from itertools import groupby
from selenium.webdriver.common.action_chains import ActionChains
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bombay_2019"]
mycol = mydb["BombayHighcourtdata_2019"]
driver = webdriver.Firefox(executable_path = './geckodriver')
driver.get('https://bombayhighcourt.nic.in/index.php')
time.sleep(5)
services = driver.find_element_by_link_text('Services')
hover = ActionChains(driver).move_to_element(services)
hover.perform()
time.sleep(5)
ordersJudgements = driver.find_element_by_link_text('Orders & Judgments')
hover_1 = ActionChains(driver).move_to_element(ordersJudgements)
hover_1.perform()
time.sleep(5)
coram_wise = driver.find_element_by_link_text('Coram Wise').click()
time.sleep(5)
cheif_justice = driver.find_elements_by_class_name('form-control')[2]
options = cheif_justice.find_elements_by_tag_name('option')
for elem in range(0,len(options)):
    print(elem)
    try:
      Select_court = driver.find_element_by_class_name('form-control')
      options = Select_court.find_elements_by_tag_name('option')[0].click()
      cheif_justice = driver.find_elements_by_class_name('form-control')[2]
      options = cheif_justice.find_elements_by_tag_name('option')
      options = cheif_justice.find_elements_by_tag_name('option')[elem].click()
      from_date = driver.find_element_by_id('demo1')
      from_date.send_keys('01-01-2019')
      to_date = driver.find_element_by_id('demo2')
      to_date.send_keys('31-12-2019')
      time.sleep(5)
      capthca = driver.find_element_by_id('captchaimg')
      capthca_1 = capthca.get_attribute('alt')
      time.sleep(5)
      captcha_send = driver.find_element_by_id('captcha_code')
      captcha_send.send_keys(capthca_1)
      time.sleep(5)
      submit_button = driver.find_elements_by_tag_name('input')[10].click()
      data = driver.find_element_by_class_name('table-responsive')
      anchor = data.find_elements_by_tag_name('a')
      td = data.find_elements_by_tag_name('tr')
      data_bombay_1 = []
      for elem_text in td:
          td_1 = elem_text.find_elements_by_tag_name('td')
          data_bombay = []
          for elem_text_1 in td_1:
              data_bombay.append(elem_text_1.text.splitlines())
          data_bombay_1.append(data_bombay)
      data_bombay_1.pop(0)
      for elem_bom in data_bombay_1:
          mydict = { "CORAM":elem_bom[0], "PARTY":elem_bom[1] ,"orderJudgementdateandbench":elem_bom[2],"Casenoandupdatedate":elem_bom[3]}
          insert = mycol.insert_one(mydict)
      for link in anchor:
          file_name = (link.text.replace('/',''))
          anchor_attribute = link.get_attribute('href')
          r = requests.get(anchor_attribute, stream=True)
          with open('./pdfdownload_bombay_court_2019/'+file_name+('.pdf'), 'wb') as f:
               f.write(r.content)
               print('Pdf Downloaded')   
      Back_button = driver.find_element_by_link_text('Back').click()
      time.sleep(5)
    except:
        print('No Record Found')
        Back_button = driver.find_element_by_link_text('Back').click()
        time.sleep(5)
     

