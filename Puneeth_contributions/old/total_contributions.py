import numpy as np
import pandas as pd
from pandas import DataFrame
import glob, os

names = []
cont = []

os.chdir("/home/puneeth/Desktop/GitHub_Mining/ContributionScrapper/GithubContributions")
for file in glob.glob("*.xlsx"):
	data = pd.read_excel(file,sheetname='sheet1')
	data = data.drop_duplicates()
	contributions = list(data['XContributions'])
	names.append(file.split('.')[0])
	cont.append(sum(contributions))

df=DataFrame({'Username':names,'XContributions':cont})
df = df[['Username','XContributions']]
df.to_excel('total_contributions.xlsx', sheet_name='sheet1', index=False)