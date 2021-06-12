import cantools
from pprint import pprint
import pdb
import numpy as np
import csv
import binascii
db = cantools.database.load_file('Updated_DB.dbc')
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



####### Node names : It includes total nodes present in the dbc file ##############
txt_file = open('final_output_9.txt','a')
nodenames=[]
for i in t4:
    nodenames.append(i.name)
txt_file.write('Nodes'+'\n')
txt_file.write(str(nodenames)+'\n')
####Transmission_message,key:node_name,value:message_name ####
Names = []
senders1 = []
Trns_final={}
for i in t3:
    Names.append(i.name)
    i1 = i.signals
    sender = i.senders
    senders1.append(sender)
    sender_1 = list(chain.from_iterable(senders1))
Trns =dict(zip(Names,sender_1))
for key, value in Trns.items(): 
   if value in Trns_final: 
       Trns_final[value].append(key) 
   else: 
       Trns_final[value]=[key] 
txt_file.write('Tx messages'+'\n')
for i in Trns_final: 
    i1 = (i, " :", Trns_final[i]) 
    txt_file.write(str(i1)+'\n')
#### Receiver_message,key:message_name,value:receivers ####
receivers1 = []
senders1 = []
Names1 = []
recv = []
for i in t3:
    i1 = i.signals
    sender = i.senders
    senders1.append(sender)
    for i2 in i1:
        
        split = (i2.receivers)
        recv.append(split)
        Names1.append(i.name)
       
Rxns =dict(zip(Names1,recv))
txt_file.write('Rx messages'+'\n')
txt_file.write(str(Rxns)+'\n')
#### Transmission_Frame_id,key:Message_name,value:frame_id ####
messagename=[]
messageframeid=[]
Txframeid={}
for i in t3:
    messagename.append(i.name)
    
    messageframeid.append(hex(i.frame_id))
Txframeid=dict(zip(messagename,messageframeid))
txt_file.write('Tx Frameids'+'\n')
txt_file.write(str(Txframeid)+'\n')   
#### Transmission_DLC_(byte Generation key:Message_name,value:dlc' ####
dlcmessagename=[]
dlc=[]
Txdlc={}
for i in t3:
    dlcmessagename.append(i.name)
    dlc.append(i.length)
Txdlc=dict(zip(dlcmessagename,dlc))
txt_file.write('Tx Dlc'+'\n')
txt_file.write(str(Txdlc)+'\n')
#### Transmission_TX_method,key:Message_name,value:TxMethod ####

Txmessagename=[]
TxMethod=[]
Txmethodtyp={}

for i in t3:
    Txmessagename.append(i.name)
    TxMethod.append(i.send_type)
Txmethodtyp=dict(zip(Txmessagename,TxMethod))
txt_file.write('Tx_method'+'\n')
txt_file.write(str(Txmethodtyp)+'\n')

    
#### Transmission_Cycle Time Generation,key:Message_name,value:TxCycletime ####
Cymessagename=[]
TxCycletime=[]
Txcycletme={}


for i in t3:
    Cymessagename.append(i.name)
    TxCycletime.append(i.cycle_time)
Txcycletme=dict(zip(Cymessagename,TxCycletime))
txt_file.write('Tx_cycle_Time'+'\n')

txt_file.write(str(Txcycletme)+'\n')


#### Reciever_signals,key:Message_name,value:receiver_Names ####
sendersm1=[]
recvm1=[]
Namesm1=[]
Rxns={}
Rxns_final={}

for i in t3:
    im1 = i.signals
    senderm = i.senders
    sendersm1.append(senderm)
    for im2 in im1:
        splitm1 = (im2.name)
        recvm1.append(splitm1)
        Namesm1.append(i.name)
        
        Rxns =dict(zip(recvm1,Namesm1))


for key, value in Rxns.items(): 
   if value in Rxns_final: 
       Rxns_final[value].append(key) 
   else: 
       Rxns_final[value]=[key] 
txt_file.write('Reciever_signals'+'\n')
for i in Rxns_final: 
    i1 = (i, " :", Rxns_final[i])
    #txt_file.write(str(i1)+'\n')

#### Reciever_signal_frame_id,key:Message_name,value:frame_id #### 
Namesm1=[]
receive_msg_frameid = []
for i in t3:
    im1 = i.signals
    senderm = i.senders
    sendersm1.append(senderm)
    for im2 in im1:
        splitm1 = (im2.name)
        Namesm1.append(i.name)
        receive_msg_frameid.append(hex(i.frame_id))
RXframeid=dict(zip(Namesm1,receive_msg_frameid))
txt_file.write('Reciever_frame_id'+'\n')
txt_file.write(str(RXframeid)+'\n')


#### python_class,key:Name_of_the_message,value:send_type,cycle_time,DLC,counter ####
class Struct:
  Allvariables_list = []

  def __init__(self, Allvariables):
     self.Allvariables = Allvariables
     self.Allvariables_list.append(self)



t3 = db.messages
txt_file.write('Structure_class'+'\n')
for i in t3:
    a = i.send_type
    b = i.name
    c = i.cycle_time
    d = i.length
    p1 = Struct((b,a,c,d,'counter'))
    for i in Struct.Allvariables_list:
        var = i.Allvariables
        var1 = (list(var))
        var2 = (var1[1:])
        var_dict = (({var1[0]:var2}))
        txt_file.write(str(var_dict)+'\n')



        




         
    







