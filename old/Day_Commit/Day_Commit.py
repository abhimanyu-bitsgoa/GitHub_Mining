import json
import urllib2
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
from github import Github
reposURL=json.load(urllib2.urlopen("https://api.github.com/repos/abhimanyu-bitsgoa/atari/stats/punch_card"))
day=[]
for x in range(7):
	day.append(0)
hour=[]
for x in range(24):
	hour.append(0)
for X in reposURL:
	if X[2]>0:
		hri=int(X[1])
		dyi=int(X[0])
		comi=int(X[2])
		hour[hri]=hour[hri]+comi
		day[dyi]=day[dyi]+comi
		print str(X[0]) + " " +str(X[1])+ " "+str(X[2])
dname=[]
for x in range(7):
	dname.append(x)
hname=[]
for x in range(24):
	hname.append(x)

objects = dname
print len(objects)
print len(day)
y_pos = np.arange(len(objects))
performance = day
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('commits')
plt.title('Day')
 
plt.show()



