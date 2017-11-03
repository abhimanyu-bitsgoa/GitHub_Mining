import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
xls_file = pd.ExcelFile('test.xlsx')
df = xls_file.parse('sheet1 1')
x=[]
x=df['A']
y=df['B']
dataList=[]
for i in range(1,32):
	dataList.append(0)
for a,b in zip(x,y):
	ind=int(a.split('-')[2])
	val=int(b)
	dataList[ind-1]=dataList[ind-1]+b
Xaxis=range(1,32)
#print len(Xaxis)
#print len(dataList)
#plt.scatter(Xaxis, dataList)
#plt.show() 
#print dataList
 
objects = Xaxis
#y_pos = np.arange(len(objects))
y_pos = objects
performance = dataList
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Commits')
plt.title('Date')
 
plt.show()
