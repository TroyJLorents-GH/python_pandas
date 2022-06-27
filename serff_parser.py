import pandas as pd

serff = pd.read_excel(joeserff.xlsx)

final = serff.pivot(index = ('Rate Effective Date*', 'Rate Expiration Date*', 'Rating Area ID*', 'Plan ID*'), columns = 'Age*', values = 'Individual Rate*').reset_index()

qone = final.loc[final['Rate Effective Date*] == '2022-01-01']
qtwo =  = final.loc[final['Rate Effective Date*] == '2022-04-01']
qthree = final.loc[final['Rate Effective Date*] == '2022-07-01']
qfour = final.loc[final['Rate Effective Date*] == '2022-10-01']

writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlswriter')
qone.to_excel(writer, sheet_name='Q1', index=False)
qtwo.to_excel(writer, sheet_name='Q2', index=False)
qthree.to_excel(writer, sheet_name='Q3', index=False)
qfour.to_excel(writer, sheet_name='Q4', index=False)
writer.close()
