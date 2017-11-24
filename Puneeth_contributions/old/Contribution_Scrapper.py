import urllib2
from pandas import DataFrame
from bs4 import BeautifulSoup

l = []
f = open('links.txt','r')
for line in f:
	l.append(str(line).strip('\n'))
f.close()
cnt = 0
for profile in l:
	filename = profile.split('/')[-1] + '.xlsx'
	quote_page = profile
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')

	date=[]
	cont=[]

	for ulTag in soup.findAll('ul',{'data-pjax':"#js-contribution-activity"}):
		for liTag in ulTag.findAll('li'):
			for aTag in liTag.findAll('a',href=True):
				quote_page = 'https://github.com' + str(aTag['href'])
				page = urllib2.urlopen(quote_page)
				soup = BeautifulSoup(page, 'html.parser')

				Cmat=soup.find('g', attrs={'transform':'translate(16, 20)'})
				for col in Cmat.findAll('g'):
					for row in col.findAll('rect'):
						date.append(row['data-date'])
						cont.append(row['data-count'])
				#		print row['data-date'] +" : "+row['data-count']
				
	df=DataFrame({'XContributions':cont,'Date':date})
	# print df
	df.to_excel(filename, sheet_name='sheet1', index=False)
	cnt += 1
	print cnt