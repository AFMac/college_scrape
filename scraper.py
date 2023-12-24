import pandas as pd
import numpy as np  
from bs4 import BeautifulSoup
import requests
import re

df = pd.read_csv('D:\\akjnm\Documents\Adam\Programming\college_scrape\colleges.csv', header=None, encoding='cp1252')
scrp_results = []
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

for x in df[0][0:10]:
    searchStr = 'https://www.google.com/search?q=' + str(x).replace(' ','+') + '+enrollment'
    #searchStr = 'https://www.google.com/search?q=amridge+university+enrollment'
    response = requests.get(searchStr, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
    if div is not None:
        m=re.search(r'">[1-9]',str(div)).span()[0]
        n=re.search(r'[0-9]<',str(div)).span()[0]
        scrp_results.append(str(div)[m+2:n+1])
    else:
        scrp_results.append('0')
    
df.insert(2,'',scrp_results)
df.to_csv('D:\\akjnm\Documents\Adam\Programming\college_scrape\college2.csv', header=None)





