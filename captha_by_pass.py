'''from selenium import webdriver
import pdb
driver1 = webdriver.Firefox(executable_path = './geckodriver')
url = ('https://main.sci.gov.in/judgments')
driver1.get(url)
#pdb.set_trace()
cpa = driver1.find_element_by_id('cap')
cpa_2 = (cpa.text)
cpa_1 = driver1.find_element_by_id('ansCaptcha')
cpa_1.send_keys(cpa_2)'''
import requests
url = 'https://main.sci.gov.in/supremecourt/2020/7419/7419_2020_36_1502_25235_Judgement_05-Jan-2021.pdf'
r = requests.get(url, stream=True)
with open('./pdfdownload_1/'+url[48:], 'wb') as f:
     f.write(r.content)
     print('done')
