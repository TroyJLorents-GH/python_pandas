import pandas as pd
import json
from pandas import json_normalize
 
f = open('data.json')
data = json.load(f)
df = json_normalize(data['compositeRates'])
 
ee = df.rate[0]
es = df.rate[1]
ec = df.rate[2]
fa = df.rate[3]
 
df['Composite Factors'] = ee/ee
df.iat[1, 2] = es/ee
df.iat[2, 2] = ec/ee
df.iat[3, 2] = fa/ee
 
carrier = data['carrierCompanyName']
plan = data['planName']
 
df['Carrier'] = carrier
df['Plan Name'] = plan
 
writer = pd.ExcelWriter(carrier + ' CompositeTest.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()
