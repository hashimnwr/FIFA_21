#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# ## Reading the CSV file

# In[2]:


df = pd.read_csv('fifa21 raw data v2.csv', low_memory = False)


# ## First 5 rows of the data frame

# In[3]:


df.head()


# ## Names of Columns

# In[4]:


df.columns


# ## Checking the Height and Weight data types

# In[5]:


df[['Height', 'Weight']].dtypes


# ## Getting the unique values of Heights

# In[6]:


df['Height'].unique()


# ## Function to Convert all the heights to floating data type and in Centimeters

# In[7]:


def convert_cm(height):
    if 'cm' in height:
        return float(height.replace('cm', ''))
    else:
        feet, inches = height.split('\'')
        feet = float(feet)
        inches = float(inches.replace('"', ''))
        return (feet * 30.48) + (inches * 2.54)


# In[8]:


df['Height'] = df['Height'].apply(convert_cm)


# In[9]:


df['Height'].unique()


# ## Getting the unique values of Heights

# In[10]:


df['Weight'].unique()


# ## Function to Convert all the weights to floating data type and in Kilograms

# In[11]:


def convert_kg(weight):
    if 'kg' in weight:
        return float(weight.replace('kg', ''))
    else:
        return round(float(weight.replace('lbs', '')) / 2.2, 2)


# In[12]:


df['Weight'] = df['Weight'].apply(convert_kg)


# In[13]:


df['Weight'].unique()


# ## Split the Combined Join Date to Day Month Year

# In[14]:


df['Joined'].head()


# In[15]:


df[['Month' ,'Day-Year']] = df['Joined'].str.split(' ', n = 1, expand = True)
df[['Day', 'Year']] = df['Day-Year'].str.split(',', n = 1, expand = True)
df.drop(columns=['Joined', 'Day-Year'], axis = 1)


# In[16]:


df[['Month', 'Day', 'Year']].head()


# ## Converting the Money to Floating data type by replacing M and K by its powers

# In[17]:


df[['Value', 'Wage', 'Release Clause']].head()


# In[18]:


df[['Value', 'Wage', 'Release Clause']].isna().sum()


# In[19]:


df[['Value', 'Wage', 'Release Clause']].isnull().sum()


# ## Function to convert Money

# In[20]:


def convert_money(money):
    if 'M' in money:
        return float(money.replace('€', '').replace('M', '')) * 1e6
    elif 'K' in money:
        return float(money.replace('€', '').replace('K', '')) * 1e3
    else:
        return float(money.replace('€', ''))


# In[21]:


df['Value'] = df['Value'].apply(convert_money)
df['Wage'] = df['Wage'].apply(convert_money)
df['Release Clause'] = df['Release Clause'].apply(convert_money)


# In[22]:


df[['Value', 'Wage', 'Release Clause']].head()


# ## Highest number of Hits

# In[23]:


df['Hits']


# In[24]:


df['Hits'] = df['Hits'].str.replace('\n', '')
df['Hits']


# ## Visualization of Number of players vs Their nationality

# In[25]:


No_of_players= df.groupby(['Nationality']).size().sort_values(axis = 0, ascending = False)
No_of_players.head(10)

No_of_players.head(10).plot(kind='bar',color='brown')
 
plt.xlabel("Nationality")
plt.ylabel("Number of players")
plt.title("Nationality of Players")
plt.show()


# ## Visualzation of Age vs number of players

# In[26]:


Age_of_players= df.groupby(['Age']).size().sort_values(axis = 0, ascending = False)

Age_of_players.plot(kind='bar',color='orange')
plt.xlabel("Age")
plt.ylabel("Number of players")
plt.title("Age of Players")
plt.show()


# ## Visualization of Number of Hits vs Player name

# In[27]:


Number_of_hits = df.groupby(['Name']).size().sort_values(axis = 0,ascending = False)

Number_of_hits.head(10).plot(kind='bar',color='green')
plt.xlabel("Name")
plt.ylabel("Hits")
plt.title("Number of Hits")
plt.show()


# ## List of Top Players

# In[28]:


Best_players = df.sort_values(['↓OVA', 'Hits'],ascending=[False, False]).head(10)

Top= Best_players[['Name', '↓OVA', 'Hits']]
Top_players=Top.head(10)
Top_players


# ## Filtering the unwanted things from the Table

# In[29]:


def remove_n(team):
    if '\n' in team:
        return team.replace('\n', '')


# In[30]:


df['Club'] = df['Club'].apply(remove_n)


# ## Number of Clubs participating in FIFA 21

# In[31]:


Teams = df['Club'].value_counts() 
Teams.count()


# ## Top 100 players

# In[32]:


best_players = df.sort_values('↓OVA',ascending = False).head(100)
best_players.head()


# ## Number of clubs to whom these top 100 players belong to

# In[33]:


Team_vals = best_players['Club'].value_counts()
Team_vals.count()


# ## Visualization of Number of best players vs Club names

# In[34]:


Team_vals.plot(kind="bar",color='purple');
plt.title("Club with Best Players");
plt.xlabel(" Club Names")
plt.ylabel("Number of Best Players")
plt.show()


# ## Conclusion
# -We got to know that most of the players are from 'England', 'Germany', 'Spain', 'France' and 'Argentina'.
# 
# -Players Age range is from 53-23 most of the players age is 23.
# 
# -Highest number of Hits is 13 by J. Rodríguez.
# 
# -Best player based on OVA and Hits is L. Messi with 93 OVA and 372 Hits
# 
# -There are 681 different Teams participated in FIFA 2021
# 
# -There are 25 Teams in FIFA 2021 with best 100 FIFA Players
# 
# -Liverpool Team has 11 players which are among best 100 FIFA players, Liverpool team has highest best player count as compared to other countries.
