import pandas as pd 
df=pd.read_csv('Medicinne_Details.csv')
df_filtered = df[['Medicine Name','Composition' ,'Uses', 'Side_effects']]
# df_filtered.to_csv('filtered_medicine_details.csv', index=False)
