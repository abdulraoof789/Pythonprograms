import csv
import os 
import glob
import pdb
import tika
tika.initVM()
import string
import re
from tika import parser
import difflib
from difflib import SequenceMatcher
csv_file = open('output_supreme_court_2019.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/pdfdownload_2019'
directory_contents = os.listdir(dir_1)
data_main_2 = []
for i in reader:
    case_id = []
    case_id.append(i[0])
    judgement_id = []
    judgement_id.append(i[1])
    case_number = []
    case_number.append(i[2])
    case_topic = []
    case_topic.append(i[3])
    case_date = []
    case_date.append(i[4])
    applicant_name = []
    applicant_name.append(i[5])
    respondent_name = []
    respondent_name.append(i[6])
    advocate_appered = []
    advocate_appered.append(i[7])
    case_ref_type = []
    case_ref_type.append(i[8])
    case_ref = []
    case_ref.append(i[9])
    bench_type = []
    bench_type.append(i[10])
    judges = []
    judges.append(i[11])
    court_id = []
    court_id.append(i[12])
    court = []
    court.append(i[13])
    case_type_id = []
    case_type_id.append(i[14])
    case_type = []
    case_type.append(i[15])
    court_law_id = []
    court_law_id.append(i[16])
    court_law = []
    court_law.append(i[17])
    user_id = []
    user_id.append(i[18])
    YearOfCase = []
    YearOfCase.append(i[19])
    ModifiedDate = []
    ModifiedDate.append(i[20])
    Dairy_Number = []
    Dairy_Number.append(i[21])
    data_excel_main = case_id+judgement_id+case_number+case_topic+case_date+applicant_name+respondent_name+advocate_appered+case_ref_type + bench_type + judges + court_id +court+case_type_id+case_type+court_law_id+court_law+user_id+YearOfCase+ModifiedDate+Dairy_Number
    data_main_2.append(data_excel_main)
data_main_2.pop(0)
for elem_1_dairy_number in data_main_2:
    elem_1 = (elem_1_dairy_number[-1].split(' '))
    for index,elem2 in enumerate(elem_1):
        if '/' in elem2:
           if len(elem_1[index-1]) == 2:
              elem_1_dairy = (elem_1[index-1][1]+'_'+elem_1[index+1])
           else:
              elem_1_dairy = (elem_1[index-1]+'_'+elem_1[index+1])
           for path, subdirs, files in os.walk(dir_1):
               for name in files:
                   if elem_1_dairy in name:
                      file_name = []
                      file_name.append(name)
                      csv_file = open('2019_pdf_location.csv','a')
                      writer = csv.writer(csv_file)
                      writer.writerow(elem_1_dairy_number+file_name)

