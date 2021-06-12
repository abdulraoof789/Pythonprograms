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
'''csv_file = open('output_supreme_court_2021.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/pdfdownload_2021'
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
    for elem in data_strip[3:]:
        print(elem)
    #data_strip_1 = (data_strip[:1])
    #for elem in data_strip_1:
        #print(elem)
#print(data_strip[3:])
#print(data_lower_1)'''
#file1 = '9863998_1985_31_1_27425_Judgement_09-Apr-2021.pdf'
file2 = 'gmentjudis44452.pdf'
file_data = parser.from_file(file2)
text = file_data['content']
data1 = text.strip('\n')
data  = data1.splitlines()
data_2 = [x.strip() for x in data if x]
#data_3 = [x for x in data_2 if x != '']
data_4 = [x for x in data_2 if len(x) != 1]
data_5 = [x.replace('\xa0','') for x in data_4 if x]
data_6 = [x.replace('\xad','') for x in data_5 if x]
flag = True
Judgement_data = []
data_pdf = []
for index,i in enumerate(data_6):
    string_1 =  "".join(i.lower().split())
    if flag:
       data_pdf.append(i)
    #if 'supremecourtofindia' in string_1:
        #flag = True
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
    #if 'versus' in string_1:
        #data_6[index+1]
list_1 = [ele.lower() for ele in data_pdf]
print(list_1)
'''for elem2 in list_1:
    array = re.findall(r'[0-9]+', elem2)
    print(array)'''
'''if len(array)>0:
       if array[0] == '7469':
          print('yes')'''
'''data_1 = []
for elem in data_strip:
    for elem1 in list_1:
        if elem in elem1:
           data_1.append(elem)
        seq=difflib.SequenceMatcher(None,ramjan ali,elem1)
        d=seq.ratio()
        percentage = ("{0:.0f}".format(d * 100))
        if int(percentage) >= 50:
           data_1.append((elem1,int(percentage)))
print(data_1)'''
#ramjan ali & ors.      ...respondent(s)
#ramjan ali
seq=difflib.SequenceMatcher(None,'ramjan ali & ors.      ','ramjan ali')
d=seq.ratio()
percentage = ("{0:.0f}".format(d * 100))
#if int(percentage) = 50:
print(percentage)
