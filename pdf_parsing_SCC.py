import glob, os
import tika
tika.initVM()
from tika import parser
import re
import pdb
import pymongo
file_data = parser.from_file('42130_2018_6_1503_15909_Judgement_13-Aug-2019.pdf')
text = file_data['content']
data1 = text.strip('\n')
data  = data1.splitlines()
data_2 = [x.strip() for x in data if x]
data_3 = [x for x in data_2 if x != '']
data_4 = [x for x in data_3 if len(x) != 1]
data_5 = [x.replace('\xa0','') for x in data_4 if x]
data_6 = [x.replace('\xad','') for x in data_5 if x]
for i in data_6:
    if 'SCC' in i:
       print(i)
