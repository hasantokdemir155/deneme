import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


veri_df=pd.read_csv('titanic.csv')
#x1=veri_df.iloc[:,0:12].head(15)
#x1=x1.drop(['PassengerId','Parch','Ticket'],axis=1)
x1=pd.DataFrame(veri_df,columns=['Sex','Survived','Pclass'])
#x1=(x1[(x1.Pclass==3)&(x1.Sex=='male')])



sex=pd.get_dummies(x1['Sex'],drop_first=True)
#sm=x1['Sex']==1
#sm=x1.set_index(["Sex", "Pclass"]).count(level="Pclass")
#(x1['Sex']).value_counts().plot.bar()
sm1=(x1['Sex']).value_counts().male
sm=(x1['Sex']).value_counts().female
y=[sm1,sm]
y1=('male','female')
#plt.scatter(sm,sm1,s=50)

irs=load_iris()
x=pd.DataFrame(irs.data)
x.columns=irs.feature_names
x['sonc']=irs.target
print(irs.target_names[1])
print(x.head())
#plt.bar(y1,y)
#plt.show()
#print(x1.groupby('Sex').count())
#df.set_index(["Person", "Single"]).count(level="Person")
print(sm,sm1)



#print(x1)
#print(sex.head())

#plt.hist(sm)
#plt.show()
x1.drop(['Sex'],axis=1,inplace=True)
x1=pd.concat([x1,sex],axis=1)
x=x1.drop(['Survived'],axis=1)
y=x1['Survived']

#plt.countplot(x1['Pclass'],x1['Survived'])
#x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,shuffle=True,random_state=64)

#lg=LogisticRegression(C=0.1,max_iter=1000)

#lg.fit(x_train,y_train)

#print(lg.score(x_test,y_test))
#print(lg.score(x_train,y_train))

#print(x1)
#print(x1.isnull().count())
#print(x1['Sex'].count())

