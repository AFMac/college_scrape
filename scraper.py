import pandas as pd
import numpy as np  

#searchStr = 'https://datausa.io/api/data?drilldowns=University&measures=Enrollment,Admissions%20Total,Applicants%20Total'
#enroll_admin = pd.read_json('D:\\akjnm\Documents\Adam\Programming\college_scrape\enroll_admin.json', orient='index')
coredata = pd.read_csv('D:\\akjnm\Documents\Adam\Programming\college_scrape\enroll_admin.csv')
engPct= []

#add concentration (by percent degrees) of engineering degrees awarded
for i in coredata['ID University']:
    searchStr = 'https://zircon.datausa.io/api/data?University=' + str(i) + '&drilldowns=CIP2&' + \
        'measures=Completions&Degree=5&Year=2021'
    df = pd.read_json(searchStr, orient='index')
    engData = pd.DataFrame(list(df.loc['data']))
    if df.size > 2:
        if not engData[engData['CIP2']=='Engineering'].empty:
            engPct.append(engData[engData['CIP2']=='Engineering']['Completions'] / engData['Completions'].sum())
        else:
            engPct.append(0)
    else:
        engPct.append(0)

coredata['engPercent']=engPct

coredata.to_csv('D:\\akjnm\Documents\Adam\Programming\college_scrape\ea_eng.csv')


#df = pd.read_json('https://zircon.datausa.io/api/data?University=232557&drilldowns=CIP2&measures=Completions&Degree=5&Year=2021', orient='index')








