from pyresparser import ResumeParser
from nameparser import HumanName
import spacy
from tika import parser
import os
import glob
from resume_parser import resumeparse
import string
nlp = spacy.load('en_core_web_sm') 
from openpyxl import Workbook
from nltk.corpus import stopwords
import nltk
import csv
import re 
import xlsxwriter
#workbook = xlsxwriter.Workbook('arrays.xlsx')
#worksheet = workbook.add_worksheet()
book = Workbook()
sheet = book.active
os.environ['TIKA_SERVER_JAR'] = 'https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.19/tika-server-1.19.jar'
csv_file_1 = open('Resume_skill.csv','r')
reader = csv.reader(csv_file_1)
data = []
for i in reader:
    data.append(i)
data.pop(0)
flattened = [val for sublist in data for val in sublist]
data_skill_1 = [x.strip() for x in flattened if x]
data_skill_2 = [x for x in data_skill_1 if x != '']
csv_file_2 = open('Education.csv','r')
reader = csv.reader(csv_file_2)
data_edu = []
for i in reader:
    data_edu.append(i)
data_edu.pop(0)
flattened = [val for sublist in data_edu for val in sublist]
data_edu_1 = [x.strip() for x in flattened if x]
data_edu_2 = [x for x in data_edu_1 if x != '']
csv_file_3 = open('company_names_1.csv','r')
reader = csv.reader(csv_file_3)
data_comp_name = []
for i in reader:
    data_comp_name.append(i)
data_comp_name.pop(0)
flattened = [val for sublist in data_comp_name for val in sublist]
data_comp_name_1 = [x.strip() for x in flattened if x]
data_comp_name_2 = [x for x in data_comp_name_1 if x != '']
csv_file_4 = open('location.csv','r')
reader = csv.reader(csv_file_4)
data_loc = []
for i in reader:
    data_loc.append(i)
data_loc.pop(0)
flattened = [val for sublist in data_loc for val in sublist]
data_loc_1 = [x.strip() for x in flattened if x]
data_loc_2 = [x for x in data_loc_1 if x != '']
os.chdir("./Resumes")
types = ('*.pdf', '*.docx') # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))
for file in files_grabbed:
    print(file)
    data1 = parser.from_file(file)
    data = ResumeParser(file).get_extracted_data()
    data_mob = resumeparse.read_file(file)
    data2 = (data1['content'])
    data3 = (data2.splitlines())
    data_rep = [x.replace('\t','') for x in data3]
    data_1 = [x.strip() for x in data_rep if x]
    data_4 = [x for x in data_1 if x != '']
    data5 = (data2.replace('(','').replace(')',''))
    data6 = (data5.split(','))
    data_7 = [x.strip() for x in data6 if x]
    data_8 = [x for x in data_7 if x != '']
    data_9 = [x.split() for x in data_8]
    flattened_1 = [val for sublist in data_9 for val in sublist]
    data_skill = []
    for i in data_skill_2:
        if i in flattened_1:
           data_skill.append(i)
    #data_edu_1 = []
    #for i in data_edu_2:
        #if i in data_4:
           #data_edu_1.append(i)
    #print(data_edu_1)
    #print(data_skill)
    data = ResumeParser(file).get_extracted_data()
    data_degree = []
    data_degree.append(data['degree'])
    list_comp_1 = [x for x in data_degree if x!= None ]
    data_final = []
    
    if len(list_comp_1)>0:
       data_final.append(list_comp_1)
       
    if not list_comp_1:
       data_pars = parser.from_file(file)
       data2 = (data1['content'])
       data_2_2 = data2.replace('\u200b','')
       data3 = (data_2_2.splitlines())
       data_rep = [x.replace('\t','') for x in data3]
       data_1 = [x.strip() for x in data_rep if x]
       data_4 = [x for x in data_1 if x != '']
       data_edu_1_2 = []
       for i in data_edu_2:
           if i in data_4:
              data_edu_1_2.append(i)
        
       if len(data_edu_1_2)>0:
          data_final.append(data_edu_1_2)
          
       if not  data_edu_1_2:
          
          data_2_1 = data2.replace('\u200b','')
          data4 = (data_2_1.split())
          data_1_4 = [x.strip() for x in data4 if x]
          data_4_1 = [x for x in data_1_4 if x != '']
          data_edus = []
          for i in data_edu_2:
              if i in data_4_1:
                 data_edus.append(i)
          if not  data_edus:
             data_edus.append('B.Tech')
          if len(data_edus)>0:
             data_final.append(data_edus)
    data_company = []
    data_comp = parser.from_file(file)
    data_comp_1 = (data_comp['content'])
    data_comp_2 = data_comp_1.replace('\u200b','')
    data_comp_3 = (data_comp_2.splitlines())
    data_rep = [x.replace('\t','') for x in data_comp_3]
    data_comp_4 = [x.strip() for x in data_rep if x]
    data_comp_5 = [x for x in data_comp_4 if x != '']
    data_comp_1_2 = []
    for i in data_comp_name_2:
        if i in data_comp_5:
           data_comp_1_2.append(i)
        
    if len(data_comp_1_2)>0:
       data_company.append(data_comp_1_2)
        
    if not  data_comp_1_2:
       data_comp_6 = data_comp_1.replace('\u200b','')
       data_comp_7 = (data_comp_6.split())
       data_comp_8 = [x.strip() for x in data_comp_7 if x]
       data_comp_9 = [x for x in data_comp_8 if x != '']
       data_compnies = []
       for i in data_comp_name_2:
           if i in data_comp_9:
              data_compnies.append(i)
       if not  data_compnies:
          data_compnies.append('Fresher')
       if len(data_compnies)>0:
          data_company.append(data_compnies)
       #print(file,data_company)
    #print(data_final)
    data_loc_punc = []
    data1 = parser.from_file(file)
    data2 = (data1['content'])
    data3 = data2.replace('\u200b','')
    data4 = (data3.split())
    data_1 = [x.strip() for x in data4 if x]
    data_4 = [x for x in data_1 if x != '']
    for elem in data_4:
        words = elem.split()
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        data_loc_punc.append(stripped) 
    #print(data_4_1)
    flattened_2 = [val for sublist in data_loc_punc for val in sublist] 
    data_loc_4 = []
    for i in data_loc_2:
        if i in flattened_2:
           data_loc_4.append(i)
    #print(file,data_loc_4)
    data1 = parser.from_file(file)
    data2 = (data1['content'])
    data3 = data2.replace('\u200b','')
    data4 = (data3.split())
    data_1 = [x.strip() for x in data4 if x]
    data_4 = [x for x in data_1 if x != '']
    lst = ['years','Year','year']
    data_exp_2 = []
    data_exp = []
    for elem1 in lst:
        for index,elem in enumerate(data_4):
            if elem1  in elem:
               data_exp.append(data_4[index-1])
    if len(data_exp)>1:
       #data_exp_1 = []
       data_exp_2.append(data_exp[0])
       #print(file,data_exp_1)
    else:
       data_exp_2.append(data_exp)
    #print(data_exp_2)
    data3 = (data_2_2.splitlines())
    data_rep = [x.replace('\t','') for x in data3]
    data_1 = [x.strip() for x in data_rep if x]
    data_4 = [x for x in data_1 if x != '']
    data_name_1 = []
    for elem in data_4:
        name_regex = re.compile("[A-Z][a-z]+ [A-Z][a-z]+")
        name_regex_1 = (name_regex.findall(elem))
        data_name_1.append(name_regex_1)
    
    
    
    if len(data_name_1[-1]) == 0 :
       data_name = []
       for index,elem in enumerate(data_4):
           doc = nlp(elem) 
           for ent in doc.ents: 
               data_name.append((ent.text, ent.label_))
    #print(data_name)
       if 'PERSON' in data_name[0]:
          data_names = data_name[0]
          data_name_1[-1].append(data_names[0])
       else:
         data_name_1[-1].append(data_4[0])
    #print(data_name_1[-1])
    
    data_mobile_number = []
    data_mobile_number.append(data_mob['phone'])
    data_email = []
    data_email.append(data['email'])
    data_skills = []
    data_skills.append(data_skill)
    data_location = []
    data_location.append(data_loc_4)
    #print(data_4[0],data['email'],data['mobile_number'],data_skill,data_final,data_company,data_loc_4,data_exp_2)
    data_main = (data_name_1[-1] + data_email + data_mobile_number + data_skills + data_final + data_company + data_location + data_exp_2)
    #print(data_main)
    data3 = data2.replace('\u200b','')
    data4_split = (data3.split())
    #print(data4)
    data_main_1 = []
    data_main_1.append(data_final+data_company+data_exp_2)
    flattened_4 = [val for sublist in data_main_1 for val in sublist]
    flattened_5 = [val for sublist in flattened_4 for val in sublist]
    #print(flattened_5)
    master = (data_name_1 + data_email+data_mobile_number+data_skill+data_loc_4+flattened_5)
    s = (master)
    temp3 = [x for x in data4_split if x not in s]
    temp4 = ' '.join(temp3)
    data_temp = []
    data_temp.append(temp4)
    #row = 0
    #for col, data in enumerate(data_main):
        #worksheet.write_column(row, col, data)
    #workbook.close()
    #print(data_temp)
    #print(data_main + data_temp)
    #sheet.append(data_temp)
    #book.save('resume_main_4.xlsx')
    csv_file_5 = open('Resume_main_8.xlsx','a')
    writer = csv.writer(csv_file_5)
    writer.writerow(data_main + data_temp)
    print(data_main)
    #sheet.append(data_main)'''
