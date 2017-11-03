import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
xls_file = pd.ExcelFile('test.xlsx')
df = xls_file.parse('sheet1 1')
x=[]
x=df['A']
y=df['B']
dataList=[]
for i in range(1,33):
	dataList.append(0)
for a,b in zip(x,y):
	ind=int(a.split('-')[2])
	val=int(b)
	dataList[ind]=dataList[ind]+b
Xaxis=range(1,33)
print len(Xaxis)
print len(dataList)
plt.scatter(Xaxis, dataList)
plt.show() 
