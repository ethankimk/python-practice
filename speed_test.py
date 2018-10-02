
# coding: utf-8

# In[5]:

##### PANDA EXAMPLE #####
import pandas as pd
dataframe = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv', usecols=range(1,5))
before = []
new = []
after = []
for row in dataframe.values:
    speed, period, warning, location_pair = row
    if location_pair == 7:
        if warning == 1:
            if period == 1:
                before.append(speed)
            elif period == 2:
                new.append(speed)
            elif period == 3:
                after.append(speed)
print("average before sign", sum(before)/len(before))
print("average new sign", sum(new)/len(new))
print("average after sign", sum(after)/len(after))


# In[ ]:



