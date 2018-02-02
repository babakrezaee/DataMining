import os
print(os.getcwd())
os.chdir('C:\\Users\') #Set working directory
print(os.getcwd())

import bs4 as bs
import requests
import urllib
import pandas as pd
import csv
import colorama
from colorama import Fore, Back, Style

df = pd.read_csv('YourCSVFile.csv',encoding = "ISO-8859-1") # Here read you CSV file and set the encoding accordingly
saved_column = df.URL #you can also use df['column_name']

urls=saved_column
urls = [x for x in saved_column if str(x) != 'nan'] # Dropping the NA rows

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',  'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

for i, url in enumerate(urls):
    try:
        file_name_html = "page-%s.html" % i 
        file_name_text = "page-%s.txt" % i
        print(str('Opened: ')+str(url))
        req = urllib.request.Request(url, headers=hdr)
        sauce=urllib.request.urlopen(req).read()
        soup=bs.BeautifulSoup(sauce,'lxml')
        body=soup.body
        for paragraph in body.find_all('p'):
            with open(file_name_html.format(url), "a" , encoding='utf-32') as file: ## Saves the content of your URL to html
                file.write(str(paragraph.text))
            with open(file_name_text.format(url), "a" , encoding='utf-16') as file: ## Saves the content of your URL to txt
                file.write(str(paragraph.text))
        print(Fore.GREEN+str('Closed: ')+str(url))
    except:
        with open("FailedURL.csv", "a" , encoding='utf-32') as f: # You for different reaons may get errors when scraping URLs, this file collect a list of failed attempts
            writer = csv.writer(f)
            writer.writerow([i,url])
            print (Fore.RED+str('Could not scrape:')+str(url))
        pass

