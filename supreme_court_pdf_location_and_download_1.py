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
import csv
import re
import pdb
csv_file_1 = open('supreme_court_2015_dates.csv','r')
reader = csv.reader(csv_file_1)
from itertools import groupby
driver = webdriver.Firefox(executable_path = './geckodriver')
url = ('https://main.sci.gov.in/judgments')
driver.get(url)
time.sleep(10)
startdate = []
enddate = []
class_1 = driver.find_element_by_link_text('Judgment Date').click()
#for i in reader:
    #startdate.append(i[0])
    #enddate.append(i[1])
#for date,date_1 in zip(startdate[1:],enddate[1:]):
time.sleep(10)
date_from = driver.find_element_by_id('JBJfrom_date').clear()
date_10 = driver.find_element_by_id('JBJfrom_date')
date_10.send_keys('03-06-2021')
date_2 = driver.find_element_by_id('JBJto_date').clear()
date_20 = driver.find_element_by_id('JBJto_date')
date_20.send_keys('03-06-2021')
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
data_2 = [] 

for elem in class_6:
    data_2.append(elem.text)
    links = elem.find_elements_by_tag_name('a')
    for lin in links:
        data_2.append(lin.get_attribute('href'))
result = [list(g) for k,g in groupby(data_2,lambda x:x=='') if not k]
csv_file_2 = open('test_for_one_date.csv','a')
for elem_data in result:
    data_link = []
    for elem_link in elem_data:
        if elem_link.endswith('.pdf'):
           data_link.append(elem_link)

    list_1 = [x for x in elem_data if not x.endswith('.pdf')]
    list_2 = (list_1+data_link)
    list_3 = [i for i in list_2 if not ('jonew' in i)]
    list_4 = [x for x in list_3 if  x.endswith('.pdf')]
    list_5 = list(dict.fromkeys(list_4))
    data_url_name = []
    for url_link in list_5:
        url_name = url_link.replace('/','')[24:]
        r = requests.get(url_link, stream=True)
        data_url_name.append(url_name)
        with open('./pdfdownload_2015/'+url_name, 'wb') as f:
             f.write(r.content)
             print('done')
             time.sleep(10)
    final_list = (list_3)
    final_list_1 = [i for i in final_list if not ('https' in i or 'http' in i)]
    date_2 = []
    date_2.append('03-06-2021')
    date_3 = []
    date_3.append('03-06-2021')
    
    writer = csv.writer(csv_file_2)
    writer.writerow(date_2+date_3+final_list_1+data_url_name)
csv_file_2.close()  
#pdb.set_trace() 
    #print(date_2+date_3+final_list_1+data_url_name)
csv_file_3 = open('test_for_one_date.csv','r')
reader = csv.reader(csv_file_3)
data = []
for i in reader:
        csv_list = [x for x in i if x]
        if len(csv_list)>0:
           case_no = (i[3].split('/'))
           case_no_1 = [x.split('-') for x in case_no]
           case_no_2 = (case_no_1[0])
           try:
              case_no_3 = (case_no_2[1].lstrip('0'))
              case_no_4 = (case_no_3.strip())
              data_case = []
              data_case.append(case_no_4)
           except:
              data_case = []
              data_case.append('Empty')
           Appelent = (i[4].split('Name'))
           Data_Appelent = []
           Data_Appelent.append(Appelent[1])
       #print(Data_Appelent)
           Respondent = (i[5].split('Name'))
           Data_Respondent = []
           Data_Respondent.append(Respondent[1])
       #print(Data_Respondent)
           Appeared_Advocate_1 = []
           Advocate = (i[6].split('Advocate'))
           petitioner_Advocate = []
           petitioner_Advocate.append(Advocate[1])
           Advocate = (i[7].split('Advocate'))
           Respondent_Advocate = []
           Respondent_Advocate.append(Advocate[1])
           pdf_link_1 = i[10]
           pdf_link = []
           pdf_link.append(pdf_link_1)
           Appeared_advocate = (petitioner_Advocate + Respondent_Advocate)
           Appeared_Advocate_1.append(Appeared_advocate)
           Bench_Type = (i[8].split(','))
           Bench_judge = []
           Bench_no_1 = [x.lstrip('Bench') for x in Bench_Type  if x]
           Bench_Type_1 = []
           if len(Bench_no_1)>= 3:
              Bench_Type_1.append('Full Bench')
           if len(Bench_no_1)== 2:
              Bench_Type_1.append('Divisional Bench')
           if len(Bench_no_1)== 1:
              Bench_Type_1.append('single bench')
           Bench_judge.append(Bench_no_1)
           Dairy_data = []
           Dairy_data.append(i[2])
           case_date = []
           case_date.append(i[1])
           case_id = []
           case_id.append('Empty')
           case_ref = []
           case_ref.append('Empty')
           judgement_id = []
           judgement_id.append('Empty')
           case_topic = []
           case_topic.append('Empty')
           case_ref_type = []
           case_ref_type.append('Empty')
           court_id = []
           court_id.append('15')
           court = []
           court.append('Supreme Court')
           case_type_id = []
           case_type_id.append('Empty')
           case_type = []
           case_type_1 = (i[3])
           if 'C.A' in case_type_1:
               case_type.append('Civil')
           if 'Crl.A' in case_type_1:
               case_type.append('Criminal')
           if 'W.P.(C)' in case_type_1:
               case_type.append('Writ petition (Civil)')
           if 'W.P.(Crl.)' in case_type_1:
              case_type.append('Writ petition (Criminal)')
           if 'CONMT.PET.(C)' in case_type_1:
               case_type.append('Contempt Petition')
           if 'R.P.(C)' in case_type_1:
               case_type.append('Review Petition (Civil)')
           if 'R.P.(Crl.)' in case_type_1:
              case_type.append('Review Petition (Cri)')
           if 'SLP(C)' in case_type_1:
              case_type.append('Special Leave Petition (Civil)')
           if 'SLP(Crl)' in case_type_1:
              case_type.append('Special leave petition (Cri)')
           if 'MA' in case_type_1:
              case_type.append('Miscc. Appln.')
           if 'T.P.(C)' in case_type_1:
              case_type.append('Transfer Petition (Civil)')
           if 'T.P.(Crl.)' in case_type_1:
              case_type.append('Transfer Petition (Criminal)')
           if 'T.C.(C)' in case_type_1:
              case_type.append('Transfer Case')
           if 'SMW(C)' in case_type_1:
              case_type.append('Suo Motu Writ Petition (C)')
           if 'ARBIT.CASE(C)' in case_type_1:
             case_type.append('Arbitration Petition')
           if 'SMW(Crl)' in case_type_1:
              case_type.append('Suo Motu Writ Petition')
           if 'SMC(Crl)' in case_type_1:
              case_type.append('Suo Motu Criminal Contempt Petition')
       #case_type.append('Empty')
           case_law_id = []
           case_law_id.append('Empty')
           case_law = []
           case_law.append('Empty')
           user_id = []
           user_id.append('Empty')
           YearOfCase = []
           YearOfCase.append('Empty')
           Modified_date = []
           Modified_date.append('Empty')
       #print(data_case+judgement_id+Data_Appelent+Data_Respondent+Appeared_Advocate_1+Bench_Type_1+Bench_judge+Dairy_data)
           csv_file = open('test_for_one_date_final.csv','a')
           writer = csv.writer(csv_file)
           writer.writerow(case_id+judgement_id+data_case+case_topic+case_date+Data_Appelent+
       Data_Respondent+Appeared_Advocate_1+case_ref_type+case_ref+Bench_Type_1+Bench_judge+court_id+court+case_type_id
       +case_type+case_law_id+case_law+user_id+YearOfCase+Modified_date+Dairy_data+pdf_link)
csv_file_3.close()      
    
