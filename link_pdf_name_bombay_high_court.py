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
csv_file = open('Bombay_high_court_input_2021_1.csv','r')
reader = csv.reader(csv_file)
dir_1 = '/home/imti/BombayHighcourtpdfs_1'
data_main_2 = []
for i in reader:
    Court = []
    Court.append(i[0])
    Journal_Reference = []
    Journal_Reference.append(i[1])
    Bench = []
    Bench.append(i[2])
    Applleant = []
    Applleant.append(i[3])
    Respondent = []
    Respondent.append(i[4])
    Judges = []
    Judges.append(i[5])
    Case_Number = []
    Case_Number.append(i[6])
    Decision_Date = []
    Decision_Date.append(i[7])
    data_excel_main = Court+Journal_Reference+Bench+Applleant+Respondent+Judges+Case_Number+Decision_Date
    data_main_2.append(data_excel_main)
data_main_2.pop(0)
for elem_list in data_main_2:
    data_lower_1 = [i.lower() for i in elem_list]
    data_strip = [i.strip() for i in data_lower_1]
    data_strip_1 = ["".join(string.split()) for string in data_strip]
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
           data1 = text.strip('\n')
           data  = text.splitlines()
           data_2 = [x.strip() for x in data if x]
           data_4 = [x for x in data_2 if len(x) != 1]
           data_5 = [x.replace('\xa0','') for x in data_4 if x]
           data_6 = [x.replace('\xad','') for x in data_5 if x]
           flag = True
           Judgement_data = []
           data_pdf = []
           for i in data_6:
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
           list_1 = [ele.lower() for ele in data_pdf]
           list_2 = ["".join(string.split()) for string in list_1]
           list_3 = [elem.replace('appellant','').replace('applicant','').replace('respondent','').replace('respondents','').replace('petitioner','') for elem in list_2]
           data_2 = []
           for elem_app_res in data_strip_1[3:5]:
               print(elem_app_res)
               if flag == True:
                  break
               for elem3 in list_3: 
                   seq=difflib.SequenceMatcher(None,elem_app_res,elem3)
                   d=seq.ratio()
                   percentage = ("{0:.0f}".format(d * 100))
                   if int(percentage) >= 70:
                      data_2.append(elem_app_res) 
           mylist = list(dict.fromkeys(data_2))
           if len(mylist)>=2:
              csv_file = open('Bombay_high_court_2021_pdf_location.csv','a')
              writer = csv.writer(csv_file)
              data_file_name = []
              data_file_name.append(name)
              writer.writerow(elem_list+data_file_name)
              print(elem_list+data_file_name)
              flag = True
              break
           #mylist = list(dict.fromkeys(data_2))
           
           #flag = True
           #break
           #if len(mylist)>=2:
              #print(mylist)
              #flag = True
              #break
'''for elem_app in data_strip_1[-2:-1]:
               for elem3 in list_2: 
                   array = elem_app
                   seq=difflib.SequenceMatcher(None,array,elem3)
                   d=seq.ratio()
                   percentage = ("{0:.0f}".format(d * 100))
                   if int(percentage) == 100:
                      print(array,percentage)
                      pdb.set_trace()'''
'''data_1 = []
                      data_1.append((array,percentage))
                      if len(data_1) == 1:
                         data_2 = []
                         for elem_app_res in data_strip[3:5]:
                             for elem3 in list_1: 
                                 seq=difflib.SequenceMatcher(None,elem_app_res,elem3)
                                 d=seq.ratio()
                                 percentage = ("{0:.0f}".format(d * 100))
                                 if int(percentage) >= 40:
                                    data_2.append(elem_app_res) 
                         data_3 = data_1 + data_2
                         if len(data_3)>=3:
                            csv_file = open('Bombay_high_court_input_pdf_location_2021.csv','a')
                            writer = csv.writer(csv_file) 
                            data_file_name = []
                            data_file_name.append(name)
                            writer.writerow(elem_list+data_file_name)'''
                                    



'''data_2 = []       
           for elem_app in data_strip[3:]:
               if flag == True:
                  break
               for elem3 in list_1:
                   seq=difflib.SequenceMatcher(None,elem_app,elem3)
                   d=seq.ratio()
                   percentage = ("{0:.0f}".format(d * 100))
                                 if int(percentage) >= 40:
                                     print("done1")
                                     data_2.append((elem_app,elem3))'''
'''for elem_case in data_strip[:1]:
              print(elem_case)
              if flag == True:
                 break
              for elem2 in list_1:
                   array = re.findall(r'[0-9]+', elem2)
                   if len(array)>0:
                      if array[0] == elem_case:
                         data_1 = []
                         data_1.append(elem_case)'''
                       # data_3 = []
'''data_2 = []

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
                            csv_file = open('output_supreme_court_2017_pdf_location.csv','a')
                            writer = csv.writer(csv_file)
                            data_file_name = []
                            data_file_name.append(name)
                            writer.writerow(elem_list+data_file_name)
                            print(elem_list)
                            flag = True
                            break'''
                                     

