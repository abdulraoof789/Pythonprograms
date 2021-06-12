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
driver = webdriver.Firefox(executable_path = '../geckodriver1')
url = ('https://islamicshop.in/men/al-shaika-arabian-thobes')
driver.get(url)
time.sleep(10)
anchor1 = driver.find_element_by_id('products-grid')
anchor = anchor1.find_elements_by_tag_name('a')
data = []
for i in anchor:
    str1 = (i.get_attribute('href'))
    if str1.endswith('.html'):
       data.append(str1)
mylist = list(dict.fromkeys(data))
for i in mylist:
    driver1 = webdriver.Firefox(executable_path = '../geckodriver1')
    driver1.get(i)
    product_heading = driver1.find_element_by_class_name('product-name')
    a = (product_heading.text)
    product_name = driver1.find_element_by_class_name('image')
    images = product_name.find_element_by_tag_name('img')
    example = images.get_attribute('src')
    price = driver1.find_element_by_class_name('price-box')
    price1 = (price.text)
    time.sleep(5)
    data1 = []
    text = driver1.find_element_by_class_name('collapse-group')
    Details = (text.text)
    data1.append(Details)
    data2 = [i.replace('\n',',') for i in data1]
    csv_file = open('tobhe_Al_shakia.csv','a')
    writer = csv.writer(csv_file)
    writer.writerow((a,data2))
    print((a,data2))
    (urllib.request.urlretrieve(example, a +".jpg"+'\n'+(price1)))
    driver1.quit()
    time.sleep(5)
    
   
