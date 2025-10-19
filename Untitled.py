#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


df = pd.read_csv('netflix_titles.csv')


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.isna()


# In[6]:


df.isna().sum()


# In[7]:


df.head()


# In[8]:


df.isna().any()


# In[9]:


df.duplicated().sum()


# In[10]:


values = {
    'director': 'Unknown',
    'cast': 'Unknown',
    'country': 'Unknown',
    'date_added': 'Unknown',
    'rating': 'Not Rated'
}

df.fillna(value=values, inplace=True)


# In[11]:


df.head()


# In[12]:


df['duration_clean'] = df['duration'].str.replace('min','').str.replace('Seasons','').str.replace('Season','')


# In[13]:


df['duration_clean'] = df['duration_clean'].astype(float)


# In[14]:


df['duration_clean']=df['duration_clean'].fillna(df['duration_clean'].mean())


# In[15]:


df['duration_clean']


# In[16]:


df.isna().sum()


# In[17]:


df.drop('duration', axis=1,inplace=True)


# In[18]:


df.isna().sum()


# In[19]:


df.head()


# In[20]:


df.rename(columns={"listed_in": "genres"}, inplace=True)


# In[21]:


df.genres


# In[22]:


df.country.head(50)


# In[23]:


def extract_country(txt):
    if pd.isna(txt):  
        return "Unknown"
    return txt.split(",")[0].strip()


# In[24]:


df["main_country"] = df["country"].apply(extract_country)


# In[25]:


df.main_country


# In[26]:


df['primary_genres'] = df['genres'].apply(lambda x: x.split(',')[0])


# In[27]:


kids = ['G', 'PG', 'PG-13', 'TV-Y', 'TV-Y7', 'TV-G', 'TV-PG']
df['age_group'] = df['rating'].apply(lambda x: 'Kids/Family' if x in kids else 'Adult')


# In[28]:


df


# In[29]:


df['type'].value_counts()


# In[30]:


df['release_year'].value_counts().sort_index()


# In[31]:


df['primary_genres'].value_counts().head(10)


# In[32]:


df['rating'].value_counts()


# In[33]:


df['main_country'].value_counts().head(10)


# In[34]:


sns.countplot(x='type', data=df, palette='Set2')
plt.title("Movies vs TV Shows on Netflix")
plt.show()


# In[35]:


df['release_year'].value_counts().sort_index().plot(kind='line', figsize=(10,6))
plt.title("Number of Titles Released per Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.show()


# In[36]:


df['main_country'].value_counts().head(10).plot(kind='bar', figsize=(10,6))
plt.title("Top 10 Countries Producing Netflix Content")
plt.show()


# In[37]:


df['primary_genres'].value_counts().head(10).plot(kind='bar', figsize=(10,6), color='skyblue')
plt.title("Top 10 Genres on Netflix")
plt.show()


# In[38]:


df['rating'].value_counts().plot(kind='bar', figsize=(10,6), color='salmon')
plt.title("Distribution of Content Ratings")
plt.show()


# In[39]:


sns.countplot(x='age_group', data=df, palette='coolwarm')
plt.title("Kids/Family vs Adult Content")
plt.show()


# In[ ]:




