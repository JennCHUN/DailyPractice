#Drawing conclusion with census_income_data.csv (on Jupyter Notebook)

import pandas as pd
% matplotlib inline 

df_census = pd.read_csv('census_income_data.csv')

#group into 2 groups 
df_a = df_census[df_census['income'] == ' >50K']
df_b = df_census[df_census['income'] == ' <=50K']

#compare the two groups in terms of education, workclass, and age
ind = df_a['education'].value_counts().index
df_a['education'].value_counts()[ind].plot(kind = 'bar');
df_b['education'].value_counts()[ind].plot(kind = 'bar');

ind = df_a['workclass'].value_counts().index
df_a['workclass'].value_counts()[ind].plot(kind = 'bar');
df_b['workclass'].value_counts()[ind].plot(kind = 'bar');

df_a['age'].hist();
df_a['age'].describe()

df_b['age'].hist();
df_b['age'].describe()

#----------------------------------------#

#Drawing conclusion with store_data.csv (on Jupyter Notebook)
## Using the grocery store dataset, create plots with appropriate labelling, colors and size to communicate the results of the following questions.
### storeA, storeB, storeC, storeD, storeE

import pandas as pd
% matplotlib inline 

df_store = pd.read_csv('store_data.csv')

#sales for the last month
df_store.tail(20)
last_month = df_store[df_store['week'] >= '2018-02-01']
last_month.iloc[:, 1:].sum().plot(kind = 'bar');
#OR 
df_store.iloc[196:, 1:].sum().plot(kind = 'bar');

#average sales
df_store.mean().plot(kind = 'barh');

#sales for the week of March 13, 3016
sales = df_store[df_store['week'] == '2016-03-13']
sales.iloc[0, 1:].plot(kind='bar');

#share of sales for the lastest 3 months
last_three_months = df_store[df_store['week'] >= '2017-12-01']
last_three_months.iloc[:, 1:].sum().plot(kind = 'pie')

