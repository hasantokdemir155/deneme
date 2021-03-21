import numpy as np
from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd
from tkinter import *
from tkinter import ttk
import numpy as np
from sklearn.preprocessing import OneHotEncoder
veri2=pd.read_csv('BankChurners.csv')
veri3=pd.read_csv('wdbc.csv')
print(veri3)


cariekr=Tk()
cariekr.geometry("500x500")


#print(veri2.feature_names)
#vr2=pd.DataFrame(veri2,columns=['Attrition_Flag', 'Customer_Age', 'Gender'
 #      ,'Education_Level', 'Marital_Status'])
#pd_df2=pd.DataFrame(pc,columns=['LatD','LatM','City'],index=[4,9,12,15])
#print(vr2.)
vr2=pd.DataFrame(veri2)

lstx2=ttk.Treeview(cariekr,height="21")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])


vr2=vr2.drop(["CLIENTNUM","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt","Total_Trans_Ct","Total_Ct_Chng_Q4_Q1","Avg_Utilization_Ratio"
              ,"Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"],axis=1)

vr2=vr2.head(20)


onehot=OneHotEncoder(handle_unknown='ignore')

onehot_ms=onehot.fit_transform(vr2["Marital_Status"].values.reshape(-1,1)).toarray()

onehot_df=pd.DataFrame(onehot_ms,columns=onehot.categories_)

vr2=vr2.join(onehot_df)

vr2.drop('Marital_Status',axis=1,inplace=True)

print(vr2.columns)


lstx2["columns"]= (vr2.columns)
#print(lstx2["columns"])
lstx2.column("#0",width = 2)




for i in lstx2["columns"]:
    lstx2.column(i,width=85)
        

for i in lstx2["columns"]:
    lstx2.heading(i,text=i)   

sm=vr2.shape

for k in range(0,sm[0]):
    for l in range(0,sm[1]):
            a=vr2.iloc[k,l]
            b=vr2.iloc[k,l+1]
            c=vr2.iloc[k,l+2]
            a1=vr2.iloc[k,l+3]
            b1=vr2.iloc[k,l+4]
            c1=vr2.iloc[k,l+5]
            a2=vr2.iloc[k,l+6]
            b2=vr2.iloc[k,l+7]
            c2=vr2.iloc[k,l+8]
            a3=vr2.iloc[k,l+9]
            b3=vr2.iloc[k,l+10]
            c3=vr2.iloc[k,l+11]
            a4=vr2.iloc[k,l+12]
            b4=vr2.iloc[k,l+13]
            c4=vr2.iloc[k,l+14]
            
            break
           
        
    lstx2.insert('',"end",text="",values=(a,b,c,a1,b1,c1,a2,b2,c2,3,b3,c3,a4,b4,c4))
lstx2.pack()



#print(vr2)

