# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 01:28:00 2020

@author: Admin
"""
#This file is going to extract all the new Growth Enterprise (ChiNext) from Shenzhen Stock Exchange (SZSE)'s CEO secretary name and email.
#The required Stock Lists are from file yl.(A list of stock name and list number excel)
from selenium import webdriver
import re
import xlrd
    
loc = (r'C:\Users\Admin\Desktop\爬虫\yl.xlsx')
yllist = xlrd.open_workbook(loc)
sheet = yllist.sheet_by_index(0) 
sheet.cell_value(0, 0) 

driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\爬虫\chromedriver_win32\chromedriver')
urlformat = "http://gg.cfi.cn/"

pagelist = [];
#input the page numbers below
for i in range(1,401): 
    print(urlformat + str(sheet.cell_value(i, 0))+".html")
    pagelist.append(urlformat + str(sheet.cell_value(i, 0))+".html");

  
url=[]
for page in pagelist:
    driver.get(page)
    list_frame = driver.find_elements(by = 'id', value = "nodea18")
    
    for li in list_frame:
        a_tag = li.find_element_by_tag_name("a")
        url.append(a_tag.get_attribute('href'))
        

msstr=[]
emailstr = []
for u in url:
    driver.get(u)
    ms = driver.find_element_by_xpath(("//table[@class = 'vertical_table']/tbody/tr[4]/td[2]"))
    print(ms.text)
    msstr.append(ms.text)
    email = driver.find_element_by_xpath(("//table[@class = 'vertical_table']/tbody/tr[7]/td[2]"))
    print(email.text)
    emailstr.append(email.text)

