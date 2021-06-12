import glob, os
import tika
tika.initVM()
from tika import parser
import re
import pdb
import pymongo
import string
import csv
import nltk
import shutil
for file in glob.glob("*.pdf"):
    file_data = parser.from_file(file)
    text = file_data['content']
    data1 = text.strip('\n')
    data  = data1.splitlines()
    data_2 = [x.strip() for x in data if x]
    data_3 = [x for x in data_2 if x != '']
    data_4 = [x for x in data_3 if len(x) != 1]
    data_5 = [x.replace('\xa0','') for x in data_4 if x]
    data_6 = [x.replace('\xad','') for x in data_5 if x]
    case_ref_data = []      
    data_pdf = []
    flag = False
    for i in data_6:
        string_1 =  "".join(i.lower().split())
        if flag:
           data_pdf.append(i)
        if 'judgment' in string_1:
             flag = True
        if 'order' in string_1:
            flag = True
        if 'corrigendum' in string_1:
            flag = True
    for i in data_pdf:
        string_1 =  "".join(i.lower().split())
        if 'v.' in string_1:
           case_ref_data.append(i)
        if 'vs.' in string_1:
           case_ref_data.append(i)
        if 'versus' in string_1:
           case_ref_data.append(i)
    print(case_ref_data)
    


'''flag = False
file_data = parser.from_file('1__Judgement_20-Feb-2019.pdf')
text = file_data['content']
data1 = text.strip('\n')
data  = data1.splitlines()
data_2 = [x.strip() for x in data if x]
data_3 = [x for x in data_2 if x != '']
data_4 = [x for x in data_3 if len(x) != 1]
data_5 = [x.replace('\xa0','') for x in data_4 if x]
data_6 = [x.replace('\xad','') for x in data_5 if x]
data_pdf = []
flag = False
for i in data_6:
    string_1 =  "".join(i.lower().split())
    if flag:
       data_pdf.append(i)
    if 'judgment' in string_1:
        flag = True
    if 'order' in string_1:
        flag = True
    if 'corrigendum' in string_1:
        flag = True
case_ref_data = []      
for i in data_pdf:
    string_1 =  "".join(i.lower().split())
    if 'v.' in string_1:
       case_ref_data.append(i)
    if 'vs.' in string_1:
       case_ref_data.append(i)
    if 'versus' in string_1:
       case_ref_data.append(i)
print(case_ref_data)'''
    #if 'Vs.' in i:
       #print(i)
