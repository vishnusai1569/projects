#!/usr/bin/env python
# coding: utf-8

# In[36]:


from numpy import *
from pandas import *


# In[37]:


dataset = read_csv("dataset_pranav.csv.xls")
X = dataset.iloc[:,[1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]].values
Y = dataset.iloc[:,-1].values


# In[38]:


dataset.describe()


# In[39]:


print(X)


# In[12]:


print(Y)


# In[13]:


Y = Y.reshape(-1,1)


# In[14]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
X = imputer.fit_transform(X)
Y = imputer.fit_transform(Y)


# In[15]:


print(X)


# In[16]:


print(Y)


# In[17]:


from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
X[:,0] = le1.fit_transform(X[:,0])
le2 = LabelEncoder()
X[:,4] = le2.fit_transform(X[:,4])
le3 = LabelEncoder()
X[:,6] = le3.fit_transform(X[:,6])
le4 = LabelEncoder()
X[:,7] = le4.fit_transform(X[:,7])
le5 = LabelEncoder()
X[:,-1] = le5.fit_transform(X[:,-1])
le6 = LabelEncoder()
Y[:,-1] = le6.fit_transform(Y[:,-1])


# In[18]:


print(X)


# In[19]:


print(Y)


# In[20]:


Y = np.array(Y,dtype=float)
print(Y)


# In[21]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)


# In[22]:


print(X)


# In[23]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)


# In[24]:


print(X_train)


# In[25]:


print(Y_train)


# In[26]:


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100,random_state=0)
classifier.fit(X_train,Y_train)


# In[27]:


classifier.score(X_train,Y_train)


# In[28]:


y_pred = le6.inverse_transform(np.array(classifier.predict(X_test),dtype=int))
Y_test = le6.inverse_transform(np.array(Y_test,dtype=int))


# In[29]:


print(y_pred)


# In[30]:


print(Y_test)


# In[31]:


y_pred = y_pred.reshape(-1,1)
Y_test = Y_test.reshape(-1,1)


# In[33]:


df = np.concatenate((Y_test,y_pred),axis=1)
dataframe = DataFrame(df,columns=['Rain on Tommorrow','Predition of Rain'])


# In[34]:


print(dataframe)


# In[35]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,y_pred)


# In[ ]:




