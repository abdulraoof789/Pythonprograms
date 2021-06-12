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
#month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
parent_dir = "/home/imti"
for file in glob.glob("*.pdf"):
    #print(file)
    file_data = parser.from_file(file)
    text = file_data['content']
    data1 = text.strip('\n')
    data  = data1.splitlines()
    data_2 = [x.strip() for x in data if x]
    data_3 = [x for x in data_2 if x != '']
    data_4 = [x for x in data_3 if len(x) != 1]
    data_5 = [x.replace('\xa0','') for x in data_4 if x]
    data_6 = [x.replace('\xad','') for x in data_5 if x]
    SCC_count = []
    data_pdf = []
    flag = False
    for i in data_6:
        string_1 =  "".join(i.lower().split())
        if flag:
           data_pdf.append(i)
        if 'supremecourtofindia' in string_1:
            flag = True
        if 'judgment' in string_1:
             flag = False
             break
        if 'order' in string_1:
            flag = False
            break
        if 'corrigendum' in string_1:
            flag = False
            break
    
    list_comp = [x.strip('unicode-escape') for x in data_pdf[0:-1]]
    r = re.compile(r'[\u0980-\u09FF]+')
    list_comp_1 = [r.sub('', x) for x in list_comp]
    x_1 = [''.join(c for c in s if c not in string.punctuation) for s in list_comp_1]
    x_2 = [x.strip() for x in x_1 if x]
    x_3 = [x for x in x_2 if x != '']
    x_4 = (x_3)
    flag = False
    data_appeals = []
    list_1 = [ele.lower() for ele in x_4]
    if len(list_1)>0:
       if 'supreme court of india' in list_1[1]:
           print('yes')
           data_appeals.append(x_4[2:])

       else:
          data_appeals.append(x_4)
    
    flat_list = [item for sublist in data_appeals for item in sublist]
    if len(flat_list)>0:
       civil_one = "".join(flat_list[0].split())
       
       if 'Jan' in file:
              string_1_2 = (file.split('_'))
              try:
                 if len(string_1_2)>4:
                     filename = (string_1_2[6].replace('.pdf',''))
                     folder_name = filename.split('-')
                     folder_name_1 = folder_name[1] + '-' + folder_name[2]
                     path = os.path.join(parent_dir, folder_name_1)
                     print(path)
                     os.mkdir(path)
                     print(folder_name_1)
                 else:
                    filename = (string_1_2[-1].replace('.pdf',''))
                    folder_name = filename.split('-')
                    folder_name_1 = folder_name[1] + '-' + folder_name[2]
                    path = os.path.join(parent_dir, folder_name_1)
                    print(path)
                    os.mkdir(path)
                    
                    print(folder_name_1)
              except:
                print('pass')
              try:
                path_1 = os.path.join(path, civil_one)
                os.mkdir(path_1)
                print(path_1)
              except:
                print('pass')
              try:
                 string_lower =  "".join(flat_list[1].lower())
                 data_2 = []
                 data_file = []
                 if 'no' in string_lower:
                     string_2 = (string_lower.split('no'))
                     strs = (string_2[1].replace('s',''))
                     data_2.append(strs.strip())
                 else:
                    string_3 = (string_lower.split())
                    if len(string_3)>0:
                        string_0 = (string_3[-3:])
                        string_98 = ''.join(string_0)
                        string_3.append(string_98)
                        data_2.append(string_3[-1])
                 string_1_2 = (file.split('_'))
                 if len(string_1_2)>4:
                     filename = (string_1_2[6].replace('.pdf',''))
                     data_file.append(filename)
                 else:
                     filename = (string_1_2[-1].replace('.pdf',''))
                     data_file.append(filename)
                     filename_1 = (data_2 + data_file)
                     filename_2 = '_'.join(filename_1)
                     print(file)
                     shutil.move(file, path_1+ '/'+filename_2+'.pdf')
                     print(filename_2)
              except:
                print('already')
              '''try:
                 string_lower =  "".join(flat_list[1].lower())
                 data_2 = []
                 data_file = []
                 if 'no' in string_lower:
                     string_2 = (string_lower.split('no'))
                     strs = (string_2[1].replace('s',''))
                     data_2.append(strs.strip())
                 else:
                    string_3 = (string_lower.split())
                    if len(string_3)>0:
                        string_0 = (string_3[-3:])
                        string_98 = ''.join(string_0)
                        string_3.append(string_98)
                        data_2.append(string_3[-1])
                 string_1_2 = (file.split('_'))
                 if len(string_1_2)>4:
                     filename = (string_1_2[6].replace('.pdf',''))
                     data_file.append(filename)
                 else:
                     filename = (string_1_2[-1].replace('.pdf',''))
                     data_file.append(filename)
                     filename_1 = (data_2 + data_file)
                     filename_2 = '_'.join(filename_1)
                     print(file)
                     shutil.move(file, path_1+ '/'+filename_2+'.pdf')
                     print(filename_2)
                     print('pillu')
                except:
                       print('already')''' 
              '''string_lower =  "".join(flat_list[1].lower())
                data_2 = []
                data_file = []
                       if 'no' in string_lower:
                          string_2 = (string_lower.split('no'))
                          strs = (string_2[1].replace('s',''))
                          data_2.append(strs.strip())
                       else:
                          string_3 = (string_lower.split())
                          if len(string_3)>0:
                             string_0 = (string_3[-3:])
                             string_98 = ''.join(string_0)
                             string_3.append(string_98)
                             data_2.append(string_3[-1])
                       string_1_2 = (file.split('_'))
                       if len(string_1_2)>4:
                          filename = (string_1_2[6].replace('.pdf',''))
                          data_file.append(filename)
                       else:
                          filename = (string_1_2[-1].replace('.pdf',''))
                          data_file.append(filename)
                       filename_1 = (data_2 + data_file)
                       filename_2 = '_'.join(filename_1)
                       print(file)
                       shutil.move(file, path_1+ '/'+filename_2+'.pdf')
                       print(filename_2)'''
                       
              
       else:
          print('no')
