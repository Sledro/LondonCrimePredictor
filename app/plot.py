# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
# Cufflinks binds plotly to pandas dataframes in IPython notebook. Read more

import plotly
plotly.tools.set_credentials_file(username='Sledro', api_key='b78t47VjKxyv1HTh9GHN')
import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')

df = pd.read_csv('/Users/sledro/Desktop/LondonCrime/Datasets with access/Cleaned.csv', parse_dates=True, index_col=1)
df.head(3)

series = df['Crime type'].value_counts()[:20]
print(series.head(3))



#series.iplot(kind='bar', yTitle='Number of Complaints', title='NYC 311 Complaints',filename='cufflinks/categorical-bar-chart')