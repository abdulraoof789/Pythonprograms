import os
import pdb
from glob import glob
os.chdir("Overall_1")
with open('/home/imti/outputsingleDataFile_final.csv', 'a') as singleFile:
     for csvFile in glob('*.csv'):
         for line in open(csvFile, 'r'):
             line_1 = (line.splitlines())
             if line_1 == ['']:
                pass
             else:
                singleFile.write(line)
                print(line)
