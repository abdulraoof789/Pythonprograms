from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv
import pdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import urllib
driver1 = webdriver.Firefox(executable_path = '../geckodriver1')
url = 'https://islamicshop.in/women/women-all-abayas-muslim-clothing/shrug-grey-black-kashibo-abaya.html'
driver1.get(url)
time.sleep(10)
product_heading = driver1.find_element_by_class_name('product-essential')
product_heading1 = product_heading.find_element_by_class_name('product-name')
a =(product_heading1.text)
product_name = driver1.find_element_by_class_name('image')
images = product_name.find_element_by_tag_name('img')
example = images.get_attribute('src')
price = driver1.find_element_by_class_name('price-box')
price1 = (price.text)
print(price1.splitlines())
time.sleep(5)
data1 = []
text = driver1.find_element_by_class_name('collapse-group')
Details = (text.text)
data1.append(Details)
data2 = [i.replace('\n',',') for i in data1]
csv_file = open('women_abayas.csv','a')
writer = csv.writer(csv_file)
writer.writerow((a,'no old price',price1,data2,url))
print((a,data2))
(urllib.request.urlretrieve(example, a +".jpg"+'\n'+(price1)))
driver1.quit()
time.sleep(5)
    
   
