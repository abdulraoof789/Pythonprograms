import csv
import os 
import glob
import pdb
import tika
tika.initVM()
from tika import parser
csv_file = open('Bombay High Court Data_ILB_03052021_Cleaned_backup_V3.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/Bombay High Court pdfs'
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
    data_excel_main = (data_excel_app+data_excel_Res+data_excel_appeal)
    data_excel_main_1 = ["".join(string.split()) for string in data_excel_main]
    data_main_2.append(data_excel_main_1)
    data_main.append(data_court+data_journal+data_bench+data_excel_app+data_excel_Res+data_excel_appeal+data_case_number+data_date)
data_main_2.pop(0)
flat_list_1 = []
for path, subdirs, files in os.walk(dir_1):
    for name in files:
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
        print(x_4)
        data_path = []
        data_path.append(os.path.join(path, name))
        for elem in data_main_2:
            if elem in x_4:
               csv_file = open('pdf_csv.csv','a')
               writer = csv.writer(csv_file)
               print(data_main+data_path)
               writer.writerow(data_main+data_path)
            else:
              print(data_main)
              csv_file = open('pdf_csv.csv','a')
              writer = csv.writer(csv_file)
              writer.writerow(data_main)
       
