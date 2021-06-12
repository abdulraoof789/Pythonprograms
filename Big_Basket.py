#!/usr/bin/env python 
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pdb
#import bs4
import requests
import time
import itertools
import json
import csv
import glob
from pdf2docx import Converter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from itertools import groupby
driver = webdriver.Firefox(executable_path = 'geckodriver')
#data_links = []
'''url = ('https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand HYD&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtBORJsPBDIyDRcelfHXOojsII2qotjI0UVsLWCq_zt4-8X5zG0WRMsaAmoQEALw_wcB')
driver.get(url)
time.sleep(10)
category = driver.find_element_by_link_text('SHOP BY CATEGORY').click()
time.sleep(5)
category_1 = driver.find_element_by_id('navBarMegaNav')
link_1 = category_1.find_elements_by_tag_name('a')
for elem in link_1:
    data_links.append(elem.get_attribute('href'))
print(data_links)'''
'''url = 'https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb'
driver.get(url)
time.sleep(10)'''
'''csd = driver.find_element_by_class_name('items')
csd_1 = csd.find_elements_by_class_name('clearfix')
for i in csd_1:
    text_1 = (i.text.splitlines())
    if len(text_1)>1:
       csv_file_1 = open('big_basket.csv','a')
       writer = csv.writer(csv_file_1)
       writer.writerow(text_1)'''

#url = 'https://www.bigbasket.com/product/all-categories/'
#driver.get(url)
#data_links = driver.find_element_by_class_name('dp_headding')
#data_links_1 = data_links.find_element_by_class_name('uiv2-search-category')
#for i in data_links:
    #tprint(i.get_attribute('href'))
url = 'https://www.bigbasket.com/cl/eggs-meat-fish/?nc=nb'
driver.get(url)
#click = driver.find_element_by_class_name('show-more').click()
#while True:
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
number_of_scroll = 6
while number_of_scroll > 0:
    
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      number_of_scroll = number_of_scroll-1
      while True:
          click = driver.find_element_by_class_name('show-more').click()
          csd = driver.find_element_by_class_name('items')
          csd_1 = csd.find_elements_by_class_name('clearfix')
          for i in csd_1:
              text_1 = (i.text.splitlines())
              if len(text_1)>1:
                 print(text_1)
                 csv_file_2 = open('big_basket_egg_meat_updated.csv','w')
                 writer = csv.writer(csv_file_2)
                 writer.writerow(text_1)

'''csv_file_2 = open('big_basket_food_oil_masalas_2.csv','a')
                writer = csv.writer(csv_file_2)
                writer.writerow(text_1)'''

'''csd = driver.find_element_by_class_name('items')
csd_1 = csd.find_elements_by_class_name('clearfix')
for i in csd_1:
    text_1 = (i.text.splitlines())
    if len(text_1)>1:
       print(text_1)'''

