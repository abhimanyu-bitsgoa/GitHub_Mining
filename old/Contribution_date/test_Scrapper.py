import urllib2
from pandas import DataFrame
from bs4 import BeautifulSoup
quote_page = 'https://github.com/GrahamCampbell'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

#price_box = soup.find('ul', attrs={'class':'filter-list small'})
#for li in price_box.findAll('li'):
##	print li.find('a').text.strip()
#	print li.find('a')['href']

#dat=price_box.find_next('li').find('a', attrs={'class':'js-year-link filter-item px-3 mb-2 py-2 selected'}).text.strip()
#print dat
date=[]
cont=[]
Cmat=soup.find('g', attrs={'transform':'translate(16, 20)'})
for col in Cmat.findAll('g'):
	for row in col.findAll('rect'):
		date.append(row['data-date'])
		cont.append(row['data-count'])
#		print row['data-date'] +" : "+row['data-count']
df=DataFrame({'XContributions':cont,'Date':date})
print df
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
