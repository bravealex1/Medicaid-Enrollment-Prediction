#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install prophet


# In[3]:


pip install matplotlib


# In[4]:


pip install pandas


# In[5]:


pip install --upgrade pandas numpy prophet


# In[6]:


pip install --upgrade pip setuptools wheel


# In[7]:


import pandas as pd
from prophet import Prophet


# In[8]:


pd.set_option('display.width', 300)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# In[9]:


df = pd.read_csv('Medicaid_data.csv', encoding = 'unicode_escape')


# In[10]:


df = df[df['final_report'] == 'Y']   # Need rows that are the final report only
df = df[df['report_date'] != '09/01/2013']    # Remove the date 09/01/2013 since it was the only date before 06/01/2017
df.dropna(subset=['total_medicaid_enrollment'], inplace=True)   # removes the rows that are empty


# In[11]:


df = df[['report_date', 'total_medicaid_enrollment']]   # Limit the columns to two only: Report date, and medicaid enrollment
df = df.groupby('report_date').agg('sum').reset_index()     # This will sum the number of medicaid enrollment for every single date
df = df.rename(columns={'report_date':'ds','total_medicaid_enrollment':'y'})    # Rename columns to the ones that Prophet require. Note: Prophet requires the date to be named as 'ds', and targeted data as 'y'
print(df.head())


# In[12]:


model = Prophet()  # Create the model
model.fit(df)      # Train the model


# In[13]:


future = model.make_future_dataframe(periods = 365 *10)


# In[14]:


forecast = model.predict(future)


# In[16]:


import matplotlib.pyplot as plt


# In[18]:


import matplotlib.pyplot as plt

# Ensure dates, yhat, yhat_lower, and yhat_upper are numpy arrays
dates_np = dates.to_numpy()
yhat_np = yhat.to_numpy()
yhat_lower_np = yhat_lower.to_numpy()
yhat_upper_np = yhat_upper.to_numpy()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot_date(dates_np, yhat_np, '-', label='Forecast', color='#0072B2')
plt.fill_between(dates_np, yhat_lower_np, yhat_upper_np, color='#0072B2', alpha=0.2)

# Additional plotting configurations if needed
# ...

plt.show()


# In[ ]:




