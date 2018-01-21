import pandas as pd

data = pd.read_csv('/Users/sledro/Desktop/LondonCrime/Datasets with access/London-street.csv', sep=',')
data.drop(data.index[0])
data.dropna().to_csv('data_clean.csv', index=None)