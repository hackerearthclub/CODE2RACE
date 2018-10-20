import pandas as pd
import numpy as np
d1=pd.Series(range(5,10))
d1=list(d1)
print(d1)
print(type(d1))


d2=pd.Series(range(4))
d3=pd.Series(range(4,8))
print(d2+d3)

data=np.array([4,6,7,8])
d4=pd.DataFrame(data)
print(d4**3)

data={ 'names':['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
d5=pd.DataFrame(data)
d5['names']=d5['names'].replace('James','Suresh')
print(d5)
print('hi')
print(d5.iloc[[1,3,5,6],[1,3]])
d5.loc[3,'score']=11.5
print(d5)
print(sum(d5['attempts']))
d1={ 'names':'suresh','attempts':2,'qualify':'no'}
d5=d5.append(d1,ignore_index=True)
print(d5)


print(d5.sort_values(by=['score'],ascending=True))

d5['qualify']=d5['qualify'].replace('yes',1)
d5['qualify']=d5['qualify'].replace('no',0)
print(d5)

del d5['attempts']
print(d5)


for index,rows in d5.iterrows():
    print(rows['names'],rows['qualify'])
