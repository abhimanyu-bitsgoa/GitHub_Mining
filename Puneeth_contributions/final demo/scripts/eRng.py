import pandas as pd
import operator
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from random import shuffle
import numpy as np
import seaborn as sns

def removeK(col):
    global df
    i=0
    for num in df[col]:
        if 'k' in num:
            df.loc[i,col] = float(df.loc[i,col].replace('k',''))*1000
            df.loc[i,col] = int(df.loc[i,col])
        i=i+1

file = pd.ExcelFile("Final_GitHub_Data.xlsx")
df = file.parse("sheet1 1")
    
removeK('Followers')
removeK('Starred')
removeK('Following')
removeK('Repositories')

df['Followers'] = pd.to_numeric(df['Followers'])
df['Years_Active'] = pd.to_numeric(df['Years_Active'])
df['Orgnisations'] = pd.to_numeric(df['Orgnisations'])
df['Following'] = pd.to_numeric(df['Following'])
df['Forked'] = pd.to_numeric(df['Forked'])
df['Starred'] = pd.to_numeric(df['Starred'])
df['Repositories'] = pd.to_numeric(df['Repositories'])
df['Contributions'] = pd.to_numeric(df['Contributions'])
df['Starred'] = pd.to_numeric(df['Starred'])



df['Followers'] = df['Followers']/df['Followers'].max()
df['Years_Active'] = df['Years_Active']/df['Years_Active'].max()
df['Orgnisations'] = df['Orgnisations']/df['Orgnisations'].max()
df['Following'] = df['Following']/df['Following'].max()
df['Forked'] = df['Forked']/df['Forked'].max()
df['Starred'] = df['Starred']/df['Starred'].max()
df['Repositories'] = df['Repositories']/df['Repositories'].max()
df['Contributions'] = df['Contributions']/df['Contributions'].max()
df['Starred'] = df['Starred']/df['Starred'].max()

df_new = df[['Username', 'Years_Active', 'Followers']].copy()
df_new['Activity'] = (df['Orgnisations']+df['Starred']+df['Following']+df['Forked']+df['Contributions']+df['Repositories'])/6

df_new.to_excel('Some.xlsx',sheet_name='Sheet1', index = False)