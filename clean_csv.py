import csv
import os 
import glob
import pdb
# import tika
# tika.initVM()
import string
import re
# from tika import parser
# import difflib
# from difflib import SequenceMatcher
csv_file = open('OUTPUT_2017.csv','r',encoding='utf-8')
reader = csv.reader(csv_file)
for i in reader:
    data_clean = []
    data_clean.append(i[7])
    data_clean_1 = [x.strip() for x in data_clean]
    for elem in data_clean_1:
       data=[]
       if elem.endswith(','):
           pillu = elem.strip(',')
           print(pillu)
           data.append(pillu)
           csv_file_1=open('new_output1.csv','a',encoding='utf-8',newline='')
           writer=csv.writer(csv_file_1)
           writer.writerow(data)
       else:
           print(elem)
           data.append(elem)
           csv_file_1=open('new_output1.csv','a',encoding='utf-8',newline='')
           writer=csv.writer(csv_file_1)
           writer.writerow(data)
