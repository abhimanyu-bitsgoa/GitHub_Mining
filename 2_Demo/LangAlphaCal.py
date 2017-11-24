import pandas as pd
import operator
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from random import shuffle
import numpy as np
import seaborn as sns
from copy import copy, deepcopy

def getLanguageAlphas(dict):
    file = pd.ExcelFile("Final_GitHub_Data.xlsx")
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
    NoLang = 50
    for Lang in sorted_LangDict[-NoLang:]:
        SelectedLanguages.append(str(Lang[0]))

    IndDict = {}

    for ind in range(NoLang):
        IndDict[SelectedLanguages[ind]]=ind

    w, h = NoLang, NoLang
    HeatMatrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(256):
        LangList = str(df['Languages'][i][1:-1]).split(", ")
        LL = []
        for Lang in LangList:
            tempLang = Lang[1:-1]
            Language, Cnt = tempLang.split(":")
            if Language in SelectedLanguages:
                LL.append(Language)
        for L1 in LL:
            for L2 in LL:
                HeatMatrix[IndDict[L1]][IndDict[L2]]+=1
    #print HeatMatrix

    for row in range(0, len(HeatMatrix)):
          for col in range(0, len(HeatMatrix[row])):
              HeatMatrix[row][col] = float(float(HeatMatrix[row][col]) / 238)
    GivLang = []
    for key, value in dict.iteritems() :
        GivLang.append(key)

    for Lang in SelectedLanguages:
        if Lang not in GivLang:
            temp = 0
            for L1 in GivLang:
                temp += dict[L1]*HeatMatrix[IndDict[L1]][IndDict[Lang]]
            dict[Lang] = float(temp)/len(GivLang)
dict = {'Java':6, 'JavaScript': 7}
getLanguageAlphas(dict)
print dict
    
# file11 = pd.ExcelFile("W_matrix.xlsx")
# df11 = file11.parse("sheet1")




# LangScore = []


# for i in range(256):
#     temp = 0
#     for key, value in dict.iteritems() :
#         temp += value * float(df11[key][i])
#     LangScore.append(temp)
    

# file2 = pd.ExcelFile("Some.xlsx")
# df2 = file2.parse("Sheet1")

# df2['LanguageScore'] = LangScore
# df2.to_excel('FinalScore.xlsx',sheet_name='Sheet1', index = False)