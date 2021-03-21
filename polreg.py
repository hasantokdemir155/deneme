import numpy as np
import pandas as pd

import matplotlib.pyplot as plt




veri2=pd.read_csv('maaslar.csv')



ver=pd.DataFrame(veri2,columns=['Egitim Seviyesi','maas'])

print(ver)

plt.plot(ver['maas'],ver['Egitim Seviyesi'])
plt.show()

x=ver['Egitim Seviyesi'].values.reshape(1,-1)
print(x)
y=ver['maas'].values.reshape(1,-1)
from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=2)

x_pl= poly_reg.fit_transform(x)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(x_pl,y)

y_pred=lr.predict(x_pl)
lr.fit(x,y)
y1_pred=lr.predict(x)

print(y_pred,y1_pred,y)
print(y1_pred([[4]]).value)

