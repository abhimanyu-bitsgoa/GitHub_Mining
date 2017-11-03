import json
import urllib2
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from github import Github

reposURL=json.load(urllib2.urlopen("https://api.github.com/users/abhimanyu-bitsgoa"))['repos_url']
repo_name=[]
rep_contri=[]
for repo in json.load(urllib2.urlopen(reposURL)):
	repo_name.append(str(repo['name']))

for name in repo_name:
	sname=name
	data=json.load(urllib2.urlopen("https://api.github.com/repos/abhimanyu-bitsgoa/"+sname+"/stats/contributors"))
	total=0
	for x in data:
		if(x['author']['login']=='abhimanyu-bitsgoa'):
			total=x['total']
	rep_contri.append(int(total))
	print sname + " : " + str(total)
objects = repo_name
print len(objects)
print len(rep_contri)
y_pos = np.arange(len(objects))
performance = rep_contri
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Commits')
plt.title('Repositories')
 
plt.show()
