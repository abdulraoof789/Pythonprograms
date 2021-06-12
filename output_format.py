import csv
import re
import pdb
csv_file_1 = open('supreme_court_pdf_doc_2016.csv','r',encoding='utf-8')
reader = csv.reader(csv_file_1)
data = []
for i in reader:
    csv_list = [x for x in i if x]
    if len(csv_list)>0:
       case_no = (i[3].split('/'))
       case_no_1 = [x.split('-') for x in case_no]
       case_no_2 = (case_no_1[0])
       try:
         case_no_3 = (case_no_2[1].lstrip('0'))
         case_no_4 = (case_no_3.strip())
         data_case = []
         data_case.append(case_no_4)
       except:
         data_case = []
         data_case.append('Empty')
       Appelent = (i[4].split('Name'))
       Data_Appelent = []
       Data_Appelent.append(Appelent[1])
       #print(Data_Appelent)
       Respondent = (i[5].split('Name'))
       Data_Respondent = []
       Data_Respondent.append(Respondent[1])
       #print(Data_Respondent)
       Appeared_Advocate_1 = []
       Advocate = (i[6].split('Advocate'))
       petitioner_Advocate = []
       petitioner_Advocate.append(Advocate[1])
       Advocate = (i[7].split('Advocate'))
       Respondent_Advocate = []
       Respondent_Advocate.append(Advocate[1])
       Appeared_advocate = (petitioner_Advocate + Respondent_Advocate)
       Appeared_Advocate_1.append(Appeared_advocate)
       Bench_Type = (i[8].split(','))
       Bench_judge = []
       Bench_no_1 = [x.lstrip('Bench') for x in Bench_Type  if x]
       Bench_Type_1 = []
       if len(Bench_no_1)>= 3:
          Bench_Type_1.append('Full Bench')
       if len(Bench_no_1)== 2:
          Bench_Type_1.append('Divisional Bench')
       if len(Bench_no_1)== 1:
          Bench_Type_1.append('single bench')
       Bench_judge.append(Bench_no_1)
       Dairy_data = []
       Dairy_data.append(i[2])
       case_date = []
       case_date.append(i[1])
       case_id = []
       case_id.append('Empty')
       case_ref = []
       case_ref.append('Empty')
       judgement_id = []
       judgement_id.append('Empty')
       case_topic = []
       case_topic.append('Empty')
       case_ref_type = []
       case_ref_type.append('Empty')
       court_id = []
       court_id.append('15')
       court = []
       court.append('Supreme Court')
       case_type_id = []
       case_type_id.append('Empty')
       case_type = []
       case_type_1 = (i[3])
       if 'C.A' in case_type_1:
          case_type.append('Civil')
       if 'Crl.A' in case_type_1:
          case_type.append('Criminal')
       if 'W.P.(C)' in case_type_1:
          case_type.append('Writ petition (Civil)')
       if 'W.P.(Crl.)' in case_type_1:
          case_type.append('Writ petition (Criminal)')
       if 'CONMT.PET.(C)' in case_type_1:
          case_type.append('Contempt Petition')
       if 'R.P.(C)' in case_type_1:
          case_type.append('Review Petition (Civil)')
       if 'R.P.(Crl.)' in case_type_1:
          case_type.append('Review Petition (Cri)')
       if 'SLP(C)' in case_type_1:
          case_type.append('Special Leave Petition (Civil)')
       if 'SLP(Crl)' in case_type_1:
          case_type.append('Special leave petition (Cri)')
       if 'MA' in case_type_1:
          case_type.append('Miscc. Appln.')
       if 'T.P.(C)' in case_type_1:
          case_type.append('Transfer Petition (Civil)')
       if 'T.P.(Crl.)' in case_type_1:
          case_type.append('Transfer Petition (Criminal)')
       if 'T.C.(C)' in case_type_1:
          case_type.append('Transfer Case')
       if 'SMW(C)' in case_type_1:
          case_type.append('Suo Motu Writ Petition (C)')
       if 'ARBIT.CASE(C)' in case_type_1:
          case_type.append('Arbitration Petition')
       if 'SMW(Crl)' in case_type_1:
          case_type.append('Suo Motu Writ Petition')
       if 'SMC(Crl)' in case_type_1:
          case_type.append('Suo Motu Criminal Contempt Petition')
       #case_type.append('Empty')
       case_law_id = []
       case_law_id.append('Empty')
       case_law = []
       case_law.append('Empty')
       user_id = []
       user_id.append('Empty')
       YearOfCase = []
       YearOfCase.append('Empty')
       Modified_date = []
       Modified_date.append('Empty')
       #print(data_case+judgement_id+Data_Appelent+Data_Respondent+Appeared_Advocate_1+Bench_Type_1+Bench_judge+Dairy_data)
       csv_file = open('output_supreme_court_2016.csv','a')
       writer = csv.writer(csv_file)
       writer.writerow(case_id+judgement_id+data_case+case_topic+case_date+Data_Appelent+
       Data_Respondent+Appeared_Advocate_1+case_ref_type+case_ref+Bench_Type_1+Bench_judge+court_id+court+case_type_id
       +case_type+case_law_id+case_law+user_id+YearOfCase+Modified_date+Dairy_data)
       
       
