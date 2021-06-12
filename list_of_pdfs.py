import glob, os
import tika
tika.initVM()
from tika import parser
#import pdb
#import os
import re
#from nltk.corpus import stopwords
#import nltk
#import csv
#nltk.download('stopwords')
'''from nltk.tokenize import word_tokenize
#os.environ['TIKA_SERVER_JAR'] = 'https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.19/tika-server-1.19.jar'
os.chdir("./pdfdownload_2018")
data_pdfs = []'''
'''for file in glob.glob("*.pdf"):
    #file1 = '223_2009_33_1501_24857_Judgement_24-Nov-2020.pdf'
    file_data = parser.from_file(file)
    data_pdfs.append(file)
    text = file_data['content']
    data1 = text.strip('\n')
    data  = data1.splitlines()
    data_2 = [x.strip() for x in data if x]
    data_3 = [x for x in data_2 if x != '']
    for i in data_3:
        str1 = '…Appellant'
        str2 = '...APPELLANT'
        if (i.count(str1)) == 1:
            appellants = i 
        else:
         if (i.count(str2)) == 1:
               appellants = i

    for i in data_3:
        str3 = '…Respondent'
        str4 = '...RESPONDENT'
        if (i.count(str3)) == 1:
            Respondent = i 
        else:
          if (i.count(str4)) == 1:
             Respondent = i 
    for i in data_3:
        str5 = 'APPEAL'
        if (i.count(str5)) == 1:
           APPEAL = i
    data_judgement = []
    flag = False
    separator = ''
    for i in data_3:
        if flag:
           data_judgement.append(i)
        if i == 'J U D G M E N T':
           flag = True
        i1 = [i2 for i2 in data_judgement if i2]
        data_jud = []
        i3 = (separator.join(i1))
        data_jud.append(i3)
        


    appeal = (APPEAL.splitlines())
    appelts = (appellants.splitlines())
    res = (Respondent.splitlines())
    data_6 = [x.replace(u'\xa0', u' ') for x in appeal+appelts+res]
    print(data_6)'''
'''csv_file = open('supreme_court_appeal_2.csv','a')
    writer = csv.writer(csv_file)
    writer.writerow(data_6+data_jud)'''
