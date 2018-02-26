# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
# Cufflinks binds plotly to pandas dataframes in IPython notebook. Read more

import plotly
plotly.tools.set_credentials_file(username='Sledro', api_key='b78t47VjKxyv1HTh9GHN')
import plotly.plotly as py
import cufflinks as cf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
#Set width of terminal output
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Define dateparse as our data sets date fornat Y-M
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
#Read data from csv and hold it in our data frame
df = pd.read_csv('/Users/sledro/Desktop/LondonCrime/Datasets with access/Cleaned.csv', parse_dates=['Month'], date_parser=dateparse)
#Group our data by the number of each type of crimes commit each month
groupedCrimes= df.set_index('Month', drop=False).groupby(pd.Grouper(level='Month', freq='M'))['Crime type'].value_counts().unstack()

#I change the dates to be integers, I am not sure this is the best way    
df['Month'] = pd.to_datetime(df['Month'])  
df['date_delta'] = (df['Month'] - df['Month'].min())  / np.timedelta64(1,'D')


model = LinearRegression()
y = groupedCrimes.Burglary
print(y.shape)
X = df[['date_delta']]
print(X.shape)
model.fit(X, y)
model.score(X, y)
coefs = zip(model.coef_, X.columns)
print ("sl = %.1f + " % model.intercept_ + \
" + ".join("%.1f %s" % coef for coef in coefs))