import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob, os
from datetime import datetime
import seaborn as sns

master = [[],[],[]] # 0-2017,1-2016,2-2015
c = 1

user = []
stdYears = [] 

os.chdir("./GithubContributions")
for file in glob.glob("*.xlsx"):
    year17 = []
    year16 = []
    year15 = []
    data = pd.read_excel(file,sheetname='sheet1')
    data = data.drop_duplicates()
    dates = list(data['Date'])
    contributions = list(data['XContributions'])
    for i in range(len(dates)):
        if(dates[i][0:4]=='2017'):
            year17.append(int(contributions[i]))
        elif(dates[i][0:4]=='2016'):
            year16.append(int(contributions[i]))
        elif(dates[i][0:4]=='2015'):
            year15.append(int(contributions[i]))
    master[0].append(np.std(year17))
    master[1].append(np.std(year16))
    master[2].append(np.std(year15))
    user.append(file)
    stdYears.append((float(np.std(year17))+float(np.std(year16))+float(np.std(year15)))/3)
    print stdYears
    c = c+1