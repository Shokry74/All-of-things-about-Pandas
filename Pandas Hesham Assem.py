#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# # Series Function and some other functions :

# In[2]:


data = pd.Series([1,2,3,4,5,6,7,8,9])
data  #Make index By himself


# In[3]:


data.describe()  # Total informations you need 


# In[4]:


data.agg(['max','min','std','mean','sum']) #you determine what you need


# ### You can Split Data :

# In[8]:


data = pd.Series([1,2,3,4,5,6,7,8,9])
print(data[1])
print("*********************")
print(data[0:6])
print("*********************")
print(data[2:8:2])
print("*********************")
print(data[3:7:2])


# ## Two ways to make index for values :

# In[10]:


data = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
data


# In[11]:


data = pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})  #by dictionary
data


# In[13]:


print(data['a'])
print(data['c'])
print(data['b'])
print(data['d'])


# ## Index Function:

# In[21]:


a = pd.Index([1,2,3,4,5,9])
b = pd.Index([1,2,6,7,8])  
print(a & b)


# In[20]:


a = pd.Index([1,2,3,4,5,9])
b = pd.Index([1,2,6,7,8])  # بياخد كله 
print(a | b)


# In[19]:


a = pd.Index([1,2,3,4,5,9])
b = pd.Index([1,2,6,7,8])  # مش بياخد المشترك في الاتنين
print(a ^ b)


# ## Graphics in Pandas:

# In[25]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot()  # default is line garph


# In[27]:


data.plot(kind = 'line')


# In[29]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9))
data.plot(kind = 'pie') # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# In[30]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot(kind = 'bar')


# In[32]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,4,8,5))
data.plot(kind = 'barh')


# In[35]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot(kind = 'hist')  # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# In[36]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot(kind = 'area')  # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# In[37]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot(kind = 'kde')  # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# In[38]:


data = pd.Series((1,2,3,4,5,6,8,1,2,5,3,4,9,6,3,2,9,6,3,1,2,4,5,6,8,4,10,6,4,8,5))
data.plot(kind = 'box')  # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# In[40]:


data = pd.Series((1,2,3,4,5,6,7,8,9))
data.plot(kind = 'box')  # شغال علي التردد والاندكس بتاع كل رقم و كام مره اتكرر   


# # DataFrame Function:

# In[41]:


import pandas as pd 
import numpy as np


# In[45]:


data = np.random.randint(1,20,size = 36).reshape(6,6)
print(data)
print('***************************************')
col = ['one','two','three','four','five','six']
rows = ['a','b','c','d','e','f']
df = pd.DataFrame(data,index = rows , columns = col)
print(df)


# ### Some queries on dataframe:

# In[46]:


df['one']


# In[47]:


df['five']


# In[71]:


print('one' in df.keys())
print('****************')
print('seven' in df.keys())
print('****************')
print('four' in df.keys())
print('****************')
print('One' in df.keys())  # one not capital


# In[73]:


print(13 in df.values)
print('****************')
print(35 in df.values)
print('****************')
print(2 in df.values)
print('****************')
print(19 in df.values)
print('****************')


# In[64]:


print(df.keys())


# In[62]:


print(df.values)


# In[57]:


df.T  #transpose


# In[74]:


df.stack()  # Take each row alone          ممممممممممممممممممممممههههههههههههههههههمممممممممممممممممممممم


# # iloc and loc Functions

# # loc Function for string // iloc Function for numbers

# In[75]:


df


# In[85]:


df.iloc[:2,:3]


# In[86]:


df.iloc[:3,:]


# In[87]:


df.iloc[2]  # row is his index = 2 


# In[88]:


df.loc['b':'d','one':'three']  # مهم جدا في عمل الاستعلامات عن البيانات اللي عندي مهم  


# In[89]:


df.loc['a':'f','one':'five']  # مهم جدا في عمل الاستعلامات عن البيانات اللي عندي مهم  


# # Series Function and dictionary to create data :

# In[102]:


w = pd.Series({'a': 5 , 'b':10 , 'c': 13 , 'd': 23 , 'e':15 })
x = pd.Series({'a': 2 , 'b':12 , 'c': 25 , 'd': 28 , 'e':19 })
y = pd.Series({'a': 6 , 'b':7 , 'c': 20 , 'd': 20 , 'e':18 })
z = pd.Series({'a': 10 , 'b':8 , 'c': 9 , 'd': 3 , 'e':16 })

df = pd.DataFrame({'Math':w ,'Physics':x , 'French':y , 'chemistry':z})
df


# In[103]:


df.iloc[:2,:3]


# In[104]:


df.loc[df.Math>10]  # اعرض هنا لما يكون الماس اكبر من 10 


# In[105]:


df.loc[df.Math>10,['Math','French']] # اعرض هنا الماس و الفرينش لما يكون الماس اكبر من 10 


# In[110]:


df.loc[df.Physics>20,['Math','French','Physics']]


# # Sorting in df:

# In[119]:


print(df.sort_values(['French'], ascending = True ))  # تصاعدي


# In[118]:


print(df.sort_values(['French'], ascending = False )) # تنازلي 


# In[120]:


print(df.sort_values(['Math'],ascending = True))


# In[121]:


print(df.sort_values(['Math'],ascending = False))


# ## Some Function in df:(max,min,sts,mean)

# In[122]:


df.max()


# In[123]:


df.min()


# In[124]:


df.std()


# In[125]:


df.mean()


# In[130]:


print(df['Math'].max())
print('************')
print(df['Physics'].min())
print('************')
print(df['French'].std())
print('************')
print(df['chemistry'].mean())


# ## correlation coefficient : corr()

# In[132]:


df.corr() # this value is between -1 and 1 


# In[133]:


df.skew()  # مقدار انحراف الارقام عن بعضها البعض 


# # How to add new columns with data from df:

# In[136]:


import numpy as np
import pandas as pd


# In[321]:


data = np.random.randint(50,100,size = 500).reshape(100,5)
rows = np.arange(0,100)
col = ['Arabic','Math','English','French','Physics']
df = pd.DataFrame(data,index = rows , columns = col)
df


# In[322]:


df['Total'] = df['Arabic'] + df['Math'] + df['English'] + df['French'] + df['Physics']
df


# In[323]:


df['Percentage'] = df["Total"]/500*100
df


# ### Some Queries :

# In[324]:


print(df.query('Total>250'))  # كله ناجح في الداتا دي علي فكره علشان كدا طلع ال 100 طالب 


# In[325]:


print(df.query('Percentage>80'))


# In[326]:


print(df.query('Percentage>80').count())  # الطلاب اللي فوق ال80 في المئه هما 29 طالب بس  


# In[327]:


print(df.query('Percentage>80 & Total > 430'))  # And


# In[328]:


print(df.query('Percentage>80 | Total > 430'))  # Or 


# In[329]:


df[(df.Arabic>90)&(df.Math>90)]  # الاوائل في الماث و العربي 


# In[330]:


df[(df.Arabic>90)&(df.Math>70)&(df.English>70)&(df.French>70)&(df.Physics>70)] # شروط ياما اوي اهي اباااي


# # To save dataframe:

# In[332]:


df.to_csv('D:\\Learn\\Hesham Asem\\Python-C\\Pandas\\StudentData.csv')


# # To merge Two tables:

# In[194]:


employee = ['Ahmed','Elsawy','Shekoo','Boody','Nosa']
group = ['HR', 'Accounting','Engineering','Translating','Accounting']
df1 = pd.DataFrame({'Employee': employee ,'Group':group})
print(df1)
print("*******************************")
salary = [20000,30000,50000,25000,60000]
brith = [2001,2001,2000,1999,2003]
df2 = pd.DataFrame({'Employee': employee ,'Salary':salary ,'Brithdate':brith})
print(df2)
print("*******************************")
data = pd.merge(df1,df2)  # لو هتكتبها كدا لازم يكون في عمود مشترك في الجدولين لازم لازم الا لو هتحدد نوع العلاقة
print(data)


# In[202]:


name = ['ahmed','sheko','boody','foma']
food =['fash','meet','rice','suger']
df1=pd.DataFrame({'Name':name,'Food':food})
print(df1)
print("***********************")
name = ['ahmed','sheko','boody','foma']
drink = ['pepsi','coca','tea','water']
df2=pd.DataFrame({'Name':name,'Drink':drink})
print(pd.merge(df1,df2))


# In[207]:


name = ['ahmed','sheko','nana','foma']
food =['fash','meet','rice','suger']
df1=pd.DataFrame({'Name':name,'Food':food})
print(df1)
print("***********************")
name = ['ahmed','sheko','boody','soso']
drink = ['pepsi','','','coca']
df2=pd.DataFrame({'Name':name,'Drink':drink})
print(pd.merge(df1,df2,how = 'inner'))  # جاب المشترك بس ما بين الجدولين بس بس بس 


# In[209]:


name = ['ahmed','sheko','nana','foma']
food =['fash','meet','rice','suger']
df1=pd.DataFrame({'Name':name,'Food':food})
print(df1)
print("***********************")
name = ['ahmed','sheko','boody','soso']
drink = ['pepsi','water','tea','coca']
df2=pd.DataFrame({'Name':name,'Drink':drink})
print(pd.merge(df1,df2,how = 'outer'))   # جاب كله يا زميلي كله اللي في الجدولين 


# In[210]:


name = ['ahmed','sheko','nana','foma']
food =['fash','meet','rice','suger']
df1=pd.DataFrame({'Name':name,'Food':food})
print(df1)
print("***********************")
name = ['ahmed','sheko','boody','soso']
drink = ['pepsi','water','tea','coca']
df2=pd.DataFrame({'Name':name,'Drink':drink})
print(pd.merge(df1,df2,how = 'right'))   #  جاب الجدول اللي علي اليمين اللي هو داتا فريم اتنين بس


# In[211]:


name = ['ahmed','sheko','nana','foma']
food =['fash','meet','rice','suger']
df1=pd.DataFrame({'Name':name,'Food':food})
print(df1)
print("***********************")
name = ['ahmed','sheko','boody','soso']
drink = ['pepsi','water','tea','coca']
df2=pd.DataFrame({'Name':name,'Drink':drink})
print(pd.merge(df1,df2,how = 'left'))   # جاب الجدول اللي علي الشمال هو الداتا فريم واحد بس


# In[212]:


employee = ['Ahmed','Elsawy','Shekoo','Boody','Nosa']
group = ['HR', 'Accounting','Engineering','Translating','Accounting']
df1 = pd.DataFrame({'Employee': employee ,'Group':group})
print(df1)
print("*******************************")
salary = [20000,30000,50000,25000,60000]
brith = [2001,2001,2000,1999,2003]
df2 = pd.DataFrame({'Employee': employee ,'Salary':salary ,'Brithdate':brith})
print(df2)
print("*******************************")
data = pd.merge(df1,df2)  # لو هتكتبها كدا لازم يكون في عمود مشترك في الجدولين لازم لازم الا لو هتحدد نوع العلاقة
print(data)


# In[223]:


data.groupby('Salary').sum()


# In[225]:


data.groupby('Salary').sum().unstack()


# In[229]:


df = pd.DataFrame({'Key':['A','B','C','A','B','C'],
                  'data1':range(6), 
                 'data2': np.random.randint(0,10,6)} , columns = ['Key',"data1",'data2'])
print(df)
print('************************')
df2 = df.groupby('Key').aggregate({'data1':'min','data2':'max'})  
#  اشمعني هنا اختار ال كي هو اللي يستخدم في الجروب باي لان ال كي مميز نقدر نميز منه اسماء العناصر الموجوده في البيانات
print(df2)
print('************************')
df3 = df.groupby('Key').aggregate({'data1':'max','data2':'min'})
print(df3)


# # Multi Index :

# In[243]:


import pandas as pd
import numpy as np


# In[238]:


index = [('california',2000),('california',2010),
        ('New York',2000),('New York',2000),
        ('Texas',2000),('Texas',2010)]
populations = [20000,25000,30000,35000,40000,45000]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations,index = index)
pop


# # To add new columns with new informations :

# In[239]:


x = [15000,20000,25000,30000,35000,40000]
pop_df = pd.DataFrame({'Total':pop,'Under18':x})
pop_df


# # other methods to create multi index tuples :

# In[250]:


data = pd.DataFrame(np.random.rand(4,2),index = [['a','b','a','b'],[1,2,1,2]],
                    columns = ['income','profit']) 
data


# In[253]:


data = {('california',2000):10000,('california',2010):15000,
         ('New York',2000):20000,('New York',2010):25000,
        ('Texas',2000):30000,('Texas',2010):35000}
df = pd.Series(data)
df


# In[257]:


index = pd.MultiIndex.from_product([[2013,2014],[1,2]],names = ['year','visit'])
columns = pd.MultiIndex.from_product([['Bob','Giudo','Sue'],['HR','Temp']],names = ['Subject','type'])
data = np.round(np.random.randn(4,6))
h_data = pd.DataFrame(data,index = index ,columns = columns)
h_data


# In[260]:


index = pd.MultiIndex.from_product([[2013,2014],[1,2]],names = ['year','visit'])
col = pd.MultiIndex.from_product([['soso','noso','hoso'],['HR','MR']],names = ['subject','type'])
data = np.round(np.random.randn(4,6))
h_data = pd.DataFrame(data,index = index ,columns = columns)
h_data


# # Pandas With String:

# In[274]:


data = ['peter','Poul','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@bo']
print(pd.Series(data).str.len())


# In[277]:


data = ['peter','Poul','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@bo']
print(pd.Series(data).str.startswith('A'))
print("**************************")
print(pd.Series(data).str.startswith('p'))
print("**************************")
print(pd.Series(data).str.startswith('M'))


# In[283]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.endswith('y'))
print("**************************")
print(pd.Series(data).str.endswith('r'))
print("**************************")
print(pd.Series(data).str.endswith('a'))


# In[285]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.find('y'))
print("**************************")
print(pd.Series(data).str.find('r'))
print("**************************")
print(pd.Series(data).str.find('a'))


# In[290]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.rjust(25))


# In[291]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.ljust(25))


# In[293]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.center(20))


# In[297]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.zfill(15))


# In[299]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.isupper())


# In[300]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.islower())


# In[301]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.istitle())


# In[302]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.isspace())


# In[303]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.isdigit())


# In[306]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.isalpha())


# In[307]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.isalnum()) # ما فيه فرغات خالص


# In[308]:


print(pd.Series(data).str.isdecimal())  # رقم عشريي


# In[309]:


print(pd.Series(data).str.isnumeric())


# In[310]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.upper())


# In[311]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.lower())


# In[315]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.capitalize())


# In[317]:


data = ['peter','Pouly','MARY',"Abdo Shokry" , '20', '90.50' ,"     " ,'Alaa', 'no@boy']
print(pd.Series(data).str.swapcase())  # بتعكس الحاله اللي عليها الداتا من كابيتال ولا سمول 


# # Pandas With files:
# # to read file and work in it 

# In[333]:


path = 'D:\\Learn\\Hesham Asem\\Python-C\\Pandas\\StudentData.csv'
data = pd.read_csv(path)
data.head(10)


# In[356]:


columnsnames = ['student','Arabic','Math','English','French','Physics','Total','Percentage']
path = 'D:\\Learn\\Hesham Asem\\Python-C\\Pandas\\StudentData.csv'
data = pd.read_csv(path,names = columnsnames)
data


# In[ ]:




