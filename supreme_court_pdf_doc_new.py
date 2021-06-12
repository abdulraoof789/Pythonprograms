import pdb
#import bs4
import requests
import time
import itertools
import json
import csv
import glob
from selenium import webdriver
from pdf2docx import Converter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
csv_file_1 = open('supreme_court_1.csv','r')
reader = csv.reader(csv_file_1)
from itertools import groupby
driver = webdriver.Chrome(executable_path = './chromedriver')
url = ('https://main.sci.gov.in/judgments')
driver.get(url)
time.sleep(10)
startdate = []
enddate = []
class_1 = driver.find_element_by_link_text('Judgment Date').click()
for i in reader:
    startdate.append(i[0])
    enddate.append(i[1])
for date,date_1 in zip(startdate[1:],enddate[1:]):
    time.sleep(10)
    date_from = driver.find_element_by_id('JBJfrom_date').clear()
    date_10 = driver.find_element_by_id('JBJfrom_date')
    date_10.send_keys(date)
    date_2 = driver.find_element_by_id('JBJto_date').clear()
    date_20 = driver.find_element_by_id('JBJto_date')
    date_20.send_keys(date_1)
    cpa = driver.find_element_by_id('cap')
    cpa_text = (cpa.text.strip())
    cpa_1 = driver.find_element_by_id('ansCaptcha')
    cpa_1.send_keys(cpa_text)
    time.sleep(10)
    class_3 = driver.find_element_by_id('JBJ')
    time.sleep(10)
    class_2_1 = driver.find_element_by_id('v_getJBJ').click()
    time.sleep(10)
    class_3 = driver.find_element_by_id('JBJ')
    class_6 = class_3.find_elements_by_tag_name('tr')
    link = []
    for elem in class_6:
        links = elem.find_elements_by_tag_name('a')
        for lin in links:
            link.append(lin.get_attribute('href'))
   
    res = []
    [res.append(x) for x in link if x not in res]
    
    data_2 = []   
    for elem in class_6:
        data_2.append(elem.text)
    result = [list(g) for k,g in groupby(data_2,lambda x:x=='') if not k]
    for data_5 in result:
        csv_file = open('supreme_court_pdf_doc_1950.csv','a',encoding='utf-8')
        date_2 = []
        date_2.append(date)
        date_3 = []
        date_3.append(date_1)
        writer = csv.writer(csv_file)
        writer.writerow(date_2+date_3+data_5+res)
        
    for url_link in res:
        r = requests.get(url_link, stream=True)
        with open('./pdfdownload_1950/'+url_link.replace('/','')[24:], 'wb') as f:
             f.write(r.content)
             print('done')
        time.sleep(10)
        
        #if 'supremecourt_vernacular' in url_link:
            #rem_dup.remove(url_link)
    
    '''for data_5,url in zip(result,rem_dup):
        data_5 += [url] 
        csv_file = open('supreme_court_pdf_doc_1.csv','a')
        writer = csv.writer(csv_file)
        date_2 = []
        date_2.append(date)
        date_3 = []
        date_3.append(date_1)
        writer.writerow(date_2+date_3+data_5)
        url_1 = url
        print(url_1)
        r = requests.get(url_1, stream=True)'''
    '''with open('./pdfdownload_1/'+url_1.replace('/','')[48:], 'wb') as f:
             f.write(r.content)
             print('done')
        time.sleep(10)'''
'''a =  glob.glob("./pdfdownload_1/*.pdf")
for pdflink in a:
    docx_file = "./docxdownload_1/"+pdflink[15:]+".docx"
    cv = Converter(pdflink)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print('converted')'''


            
