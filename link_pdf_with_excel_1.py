import csv
import os 
import glob
import pdb
import tika
tika.initVM()
import string
import re
from tika import parser
csv_file = open('path_testing.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/BombayHighcourtpdfs_1'
directory_contents = os.listdir(dir_1)
data_main_2 = []
data_main = []
for i in reader:
    data_excel_app = []
    data_excel_Res = []
    data_excel_appeal = []
    data_court = []
    data_court.append(i[0])
    data_journal = []
    data_journal.append(i[1])
    data_bench = []
    data_bench.append(i[2])
    data_case_number = []
    data_case_number.append(i[6])
    data_date = []
    data_date.append(i[7])
    data_excel_app.append(i[3])
    data_excel_Res.append(i[4])
    data_excel_appeal.append(i[5])
    data_excel_main = (data_excel_app+data_excel_Res)
    data_excel_main_1 = ["".join(string.split()) for string in data_excel_main]
    data_main_2.append(data_excel_main_1)
    data_main.append(data_court+data_journal+data_bench+data_excel_app+data_excel_Res+data_excel_appeal+data_case_number+data_date)


data_main_2.pop(0)
for path, subdirs, files in os.walk(dir_1):
    for name in files:
        print(name)
        file_data = parser.from_file(os.path.join(path, name))
        text = file_data['content']
        data1 = text.strip('\n')
        data  = data1.splitlines()
        data_2 = [x.strip() for x in data if x]
        data_3 = [x for x in data_2 if x != '']
        data_4 = [x for x in data_3 if len(x) != 1]
        data_5 = [x.replace('\xa0','') for x in data_4 if x]
        data_6 = [x.replace('\xad','') for x in data_5 if x]
        x_2 = [x.strip() for x in data_6 if x]
        x_3 = [x for x in x_2 if x != '']
        x_4 = ["".join(string.split()) for string in x_3]
        x_5 = [i.lower() for i in x_4]
        x_6 = [''.join(c for c in s if c not in string.punctuation) for s in x_5]
        for elem in data_main_2:
            list_2 = [i.lower() for i in elem]
            excel = [''.join(c for c in s if c not in string.punctuation) for s in list_2]
            excel_1 = ["".join(string.split()) for string in excel]
            l4 = [y for x in excel_1 for y in x_6 if x in y]
            l5 = [x for x in l4 if x in x_6]
            data_path = []
            data_path.append(os.path.join(path, name))
            if l4 == l5:
               csv_file = open('data_path_1.csv','a')
               writer = csv.writer(csv_file)
               writer.writerow(l5 + data_path)
            #if excel == s_1:
               #data_path = []
               #data_path.append(os.path.join(path, name))
               #print(data_path)
               #csv_file = open('data_path.csv','a')
               #writer = csv.writer(csv_file)
               #writer.writerow(s_1 + data_path)
            #else:
               #print('not matched')'''
        

'''file_data = parser.from_file('BombayHighcourtpdfs_1/pdfdownload_bombay_2021/APEAL11072004.pdf')
text = file_data['content']
data1 = text.strip('\n')
data  = data1.splitlines()
data_2 = [x.strip() for x in data if x]
data_3 = [x for x in data_2 if x != '']
data_4 = [x for x in data_3 if len(x) != 1]
data_5 = [x.replace('\xa0','') for x in data_4 if x]
data_6 = [x.replace('\xad','') for x in data_5 if x]
x_2 = [x.strip() for x in data_6 if x]
x_3 = [x for x in x_2 if x != '']
x_4 = ["".join(string.split()) for string in x_3]
x_5 = [i.lower() for i in x_4]
x_6 = [''.join(c for c in s if c not in string.punctuation) for s in x_5]
list_1 = ['ANAND MURLIDHAR SALVI','STATE OF MAHARASHTRA']
list_2 = [i.lower() for i in list_1]
excel = [''.join(c for c in s if c not in string.punctuation) for s in list_2]
excel_1 = ["".join(string.split()) for string in excel]
l4 = [y for x in excel_1 for y in x_6 if x in y]
l5 = [x for x in l4 if x in x_6]
if l4 == l5:
   print('yes')'''
'''for elem in l4:
    if elem in x_6:
       print('yes')'''
#set_1 = (set(l4))
#s_1 = list(set_1)
#s_1.sort()
#list_fi = (set(excel_1))

        
