import pandas as pd 
import matplotlib.pyplot as plt

dataset = pd.read_csv('/Users/sledro/Desktop/LondonCrime/Datasets with access/London-street.csv')

#Drop columns indexed 0,2,3,7,8,11 as invaluable data
dataset.drop(dataset.columns[[0,2,3,7,8,11]], axis=1, inplace=True)

#Drop NaN's
NaNsRemovedAndColsDropped = dataset.dropna(axis=0, how='any')

#Print first 5 rows
###print(NaNsRemovedAndColsDropped.head())

#Add data frame to json file to allow Firebase upload
#NaNsRemovedAndColsDropped.to_csv('/Users/sledro/Desktop/LondonCrime/Datasets with access/Cleaned.csv')

# https://github.com/firebase/firebase-import
# firebase-import --database_url https://londoncrimepredictor.firebaseio.com/ --path / --json Cleaned.json

#res = pd.read_json('/Users/sledro/Desktop/LondonCrime/Datasets with access/Cleaned.json', orient='records')

#print(res.head())
colors = ['#105B63', '#FFFAD5','#FFD34E','#DB9E36','#BD4932']
plot1 = NaNsRemovedAndColsDropped.groupby('Month').size().reset_index(name='number of outcomes').set_index('Month')
plot1
plot1.plot(kind="line",figsize=(20,10), linestyle='--', marker='o',color=colors)
plt.show()