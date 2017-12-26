
# coding: utf-8

# In[6]:


import csv
f = open("guns.csv","r")
data = list(csv.reader(f))
data[0:5]


# In[7]:


headers = data[0]
headers


# In[8]:


data = data[1:]
data[0:3]


# In[9]:


years = [row[1] for row in data]
years[0:5]


# In[13]:


year_counts = {}
for each in years:
    if each in year_counts:
        year_counts[each] +=1
    else:
        year_counts[each] = 1
    
year_counts        


# In[11]:


import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]


# In[10]:


dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]


# In[12]:


dates[:5]


# In[13]:


date_counts = {}
for each in dates:
    if each in date_counts:
       date_counts[each] += 1
    else:
        date_counts[each] = 1
#date_counts        
    


# In[14]:


sex_counts = {}
for each in data:
    sex = each[5]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
sex_counts


# In[16]:


race_counts = {}
for each in data:
    race = each[7]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
race_counts


# In[15]:


f = open("census.csv","r")
census = list(csv.reader(f))
census[0:5]


# In[18]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = v / mapping[k] * 100000
    
race_per_hundredk


# In[19]:


intents = [row[3] for row in data]


# In[20]:


races = [row[7] for row in data]


# In[27]:


homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1


# In[28]:


homicide_race_counts


# In[29]:


homicide_race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    homicide_race_per_hundredk[k] = v / mapping[k] * 100000
    
homicide_race_per_hundredk


# ## Findings
# It appears that gun related homicides in the US disproportionately affect people in the Black and Hispanic racial categories.
# Some areas to investigate further:
# 
# 1.The link between month and homicide rate.
# 
# 2.Homicide rate by gender.
# 
# 3.The rates of other intents by gender and race.
# 
# 4.Gun death rates by location and education.

# In[32]:




