import pandas as pd
import operator
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from random import shuffle
import numpy as np
import seaborn as sns

file = pd.ExcelFile("GitHub_Data.xlsx")
df = file.parse("sheet1 1")
LangDict = {}
for i in range(256):
	LangList = str(df['Languages'][i][1:-1]).split(", ")
	for Lang in LangList:
		tempLang = Lang[1:-1]
		Language, Cnt = tempLang.split(":")
		if Language in LangDict:
			LangDict[Language] += int(Cnt)
		else:
			LangDict[Language] = int(Cnt)

sorted_LangDict = sorted(LangDict.items(), key=operator.itemgetter(1))

SelectedLanguages = []

for Lang in sorted_LangDict[-12:]:
	SelectedLanguages.append(str(Lang[0]))
shuffle(SelectedLanguages)

LangFreq = []

for Lang in SelectedLanguages:
	LangFreq.append(int(LangDict[Lang]))

print SelectedLanguages
print LangFreq

objects = SelectedLanguages
y_pos = np.arange(len(objects))
performance = LangFreq
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()