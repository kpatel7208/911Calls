import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('911.csv')

df.info()

df.head(3)

# top 5 zipcodes for 911 calls

df['zip'].value_counts().head(5)

# top 5 townships (twp) for 911 calls

df['twp'].value_counts().head(5)

df['title'].nunique()

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# most common Reason for a 911 call

df['Reason'].value_counts()

# Seaborn to create a countplot of 911 calls by Reason

sns.countplot(x='Reason',data=df,palette='viridis')

type(df['timeStamp'].iloc[0])

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)

sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

byMonth = df.groupby('Month').count()
byMonth.head()
byMonth['twp'].plot()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

df['Date']=df['timeStamp'].apply(lambda t: t.date())

# counts of 911 calls

df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()

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

