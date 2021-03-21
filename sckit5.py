import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression




veri=pd.read_csv('vercal.csv',sep=';')

vr=pd.DataFrame(veri)

vr=vr.drop(['ID','Motorway'],axis=1)
print(vr.isnull().sum())
print(vr.eq(0).sum())
