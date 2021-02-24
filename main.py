# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#!/usr/bin/env python
# coding: utf-8

# # 911 Calls

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('911.csv')


# In[4]:


df.info()


# In[5]:


df.head(3)


# top 5 zipcodes for 911 calls

# In[6]:


df['zip'].value_counts().head(5)


# top 5 townships (twp) for 911 calls

# In[7]:


df['twp'].value_counts().head(5)


# In[31]:


df['title'].nunique()


# In[32]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# most common Reason for a 911 call

# In[33]:


df['Reason'].value_counts()


# Seaborn to create a countplot of 911 calls by Reason

# In[34]:


sns.countplot(x='Reason',data=df,palette='viridis')


# In[35]:


type(df['timeStamp'].iloc[0])


# In[36]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[37]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[38]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[39]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[40]:


sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[41]:


sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[43]:


byMonth = df.groupby('Month').count()
byMonth.head()


# In[44]:



byMonth['twp'].plot()


# In[8]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[46]:


df['Date']=df['timeStamp'].apply(lambda t: t.date())


# counts of 911 calls

# In[47]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[48]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[49]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[50]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()





plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')





sns.clustermap(dayHour,cmap='viridis')





dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()





plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')





sns.clustermap(dayMonth,cmap='viridis')

