import cantools
from pprint import pprint
import pdb
import numpy as np
import csv
import binascii
db = cantools.database.load_file('Updated_DB.DBC')
from itertools import chain
t3=db.messages
t4=db.nodes
message_nodes=[]
Txmessage_names=[]
nodesenders=[]
Txmessagenmes={}
Rxframeid={}
Urxmessages=[]
Urxmessagesframeid=[]
signa=[]
msgsender=[]
msgsignals={}

#txt_file = open('final_output_9.txt','a')
nodenames=[]
for i in t4:
    nodenames.append(i.name)
print(nodenames)
#txt_file.write('Nodes'+'\n')
#txt_file.write(str(nodenames)+'\n')
####Transmission_message,key:node_name,value:message_name #
