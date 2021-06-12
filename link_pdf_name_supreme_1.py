import csv
import os 
import glob
import pdb
import time
import tika
tika.initVM()
import string
import re
from tika import parser
import difflib
from difflib import SequenceMatcher
csv_file = open('output_supreme_court_2015.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/pdfdownload_2015'
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
for elem_list in data_main_2:
    data_lower_1 = [i.lower() for i in elem_list[2:7]]
    data_strip = [i.strip() for i in data_lower_1]
    flag = False
    for path, subdirs, files in os.walk(dir_1):
        if flag == True:
           break
        for name in files:
           if flag == True:
              break
           file_data = parser.from_file(os.path.join(path, name))
           text = file_data['content']
           print(name)
           try:
              data1 = text.strip('\n')
              data  = text.splitlines()
              data_2 = [x.strip() for x in data if x]
              data_4 = [x for x in data_2 if len(x) != 1]
              data_5 = [x.replace('\xa0','') for x in data_4 if x]
              data_6 = [x.replace('\xad','') for x in data_5 if x]

              Judgement_data = []
              data_pdf = []
              for i in data_6:
                  string_1 =  "".join(i.lower().split())
                  if flag:
                     data_pdf.append(i)
                  if 'supremecourtofindia' in string_1:
                     flag = True
                  if 'judgment' in string_1:
                     flag = False
                     break
                  if 'judgement' in string_1:
                     flag = False
                     break
                  if 'order' in string_1:
                     flag = False
                     break
                  if 'corrigendum' in string_1:
                     flag = False
                     break
              list_1 = [ele.lower() for ele in data_pdf]
              list_2 = [i.split() for i in list_1]
              for elem_case in data_strip[:1]:
                  print(elem_case)
                  if flag == True:
                     break
                  for elem2 in list_1:
                      array = re.findall(r'[0-9]+', elem2)
                      if len(array)>0:
                         if array[0] == elem_case:
                            data_1 = []
                            data_1.append(elem_case)
                            data_2 = []
                            for elem_app in data_strip[3:]:
                                if flag == True:
                                   break
                                for elem3 in list_1:
                                    seq=difflib.SequenceMatcher(None,elem_app,elem3)
                                    d=seq.ratio()
                                    percentage = ("{0:.0f}".format(d * 100))
                                    if int(percentage) >= 40:
                                       print("done1")
                                       data_2.append((elem_app,elem3))
                            data_3 = data_1 + data_2
                            if len(data_3)>=2:
                               csv_file_1 = open('output_supreme_court_2015_pdf_location.csv','a')
                               writer = csv.writer(csv_file_1)
                               data_file_name = []
                               data_file_name.append(name)
                               writer.writerow(elem_list+data_file_name)
                               print(elem_list)
                               flag = True
                               break
                            else:
                               csv_file_2 = open('output_supreme_court_2015_pdf_location_not_found.csv','a')
                               writer = csv.writer(csv_file_2)
                               writer.writerow(elem_list)
                               print(elem_list)
           except:
               print('File is Empty')                      

