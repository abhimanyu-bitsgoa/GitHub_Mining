import urllib2
from pandas import DataFrame
from bs4 import BeautifulSoup
import math
# quote_page = 'https://github.com/'+username
# page = urllib2.urlopen(quote_page)
# soup = BeautifulSoup(page, 'html.parser')

repoNumC=[]
starNumC=[]
followerNumC=[]
followingNumC=[]
orgNameC=[]
locationNameC=[]
mailIdC=[]
webUrlC=[]
orgListC=[]
bioC=[]
yearsActiveC=[]
pinnedRepoC=[]
repoLanguagesC=[]
forkedReposC=[]
usernameC=[]
repoNumG=25;

def getText(obj):
    if obj:
        return obj.text.strip()
    else:
        return "***"
def generateOverview(username):
    
    quote_page = 'https://github.com/'+username
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    
    repoNum=soup.find('a',attrs={'href':'/'+username+'?tab=repositories'}).find('span')
    starNum=soup.find('a',attrs={'href':'/'+username+'?tab=stars'}).find('span')
    followerNum=soup.find('a',attrs={'href':'/'+username+'?tab=followers'}).find('span')
    followingNum=soup.find('a',attrs={'href':'/'+username+'?tab=following'}).find('span')

    orgName=soup.find('span',attrs={'class':'p-org'})
    if orgName:
        orgName=orgName.find('div')
    locationName=soup.find('span',attrs={'class':'p-label'})
    mailId=soup.find('svg',attrs={'class':'octicon octicon-mail'})
    webUrl=soup.find('a',attrs={'class':'u-url'})
    orgList=soup.find('div',attrs={'class':'border-top py-3 clearfix'})
    bio=soup.find('div',attrs={'class':'p-note user-profile-bio'})
    yearsActive=soup.find('ul',attrs={'class':'filter-list small'})
    pinnedRepo=soup.find('ol',attrs={'class':'pinned-repos-list  mb-4 js-pinned-repos-reorder-list'})
    
    global repoNumC
    global starNumC
    global followerNumC
    global followingNumC
    global orgNameC
    global locationNameC
    global mailIdC
    global webUrlC
    global orgListC
    global bioC
    global yearsActiveC
    global pinnedRepoC
    
    repoNumC.append(getText(repoNum))
    starNumC.append(getText(starNum))
    followerNumC.append(getText(followerNum))
    followingNumC.append(getText(followingNum))
    orgNameC.append(getText(orgName))
    locationNameC.append(getText(locationName))
#     webUrlC.append(getText(webUrl))
#     print getText(repoNum)
#     print getText(starNum)
#     print getText(followerNum)
#     print getText(followingNum)
#     print getText(orgName)
#     print getText(locationName)
#     print getText(webUrl)
    if webUrl:
        webUrlC.append(1)
    else:
        webUrlC.append(0)

    if mailId:
        mailIdC.append(1)
    else:
        mailIdC.append(0)

    if bio:
        bioC.append(1)
    else:
        bioC.append(0)

    if orgList:
        orgListC.append(len(orgList.findAll('a')))
    else:
        orgListC.append(0)
        
    if yearsActive:
        yearsActiveC.append(len(yearsActive.findAll('li')))
    else:
        yearsActiveC.append(0)
    
    if pinnedRepo:
        pinnedRepoC.append(len(pinnedRepo.findAll('li')))
    else:
        pinnedRepoC.append(0)                   

    global repoNumG
    if repoNum:
    	if repoNum.text.strip()[-1]=='k':
    		repoNumG = int(float(repoNum.text.strip()[:-1])*1000)
    	else:
        	repoNumG=int(repoNum.text.strip())



# generateOverview(username)

def generateRepo(username):
    repoLanguages={}
    forkedRepos=0
    global repoLanguagesC
    global forkedReposC
    global repoNumG
    for i in range(1,int(math.ceil(repoNumG)+1)):
        quote_page = 'https://github.com/'+username+'?page='+str(i)+'&tab=repositories'
        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        repoList=soup.find('ul',attrs={'data-filterable-for':'your-repos-filter'})
        if repoList:
            for repo in repoList.findAll('li'):
                if(repo.find('span',attrs={'class':'f6 text-gray mb-1'})):
                    forkedRepos=forkedRepos+1
                language=repo.find('span',attrs={'itemprop':'programmingLanguage'})
                if language:
                    language=language.text.strip()
                    if language in repoLanguages:
                        repoLanguages[language]=repoLanguages[language]+1
                    else:
                        repoLanguages[language]=1;

    langTuple=[]
    for key in repoLanguages:
        langTuple.append(key.encode("utf-8")+":"+str(repoLanguages[key]))
    repoLanguagesC.append(langTuple)
    forkedReposC.append(forkedRepos)

usernameData = [line.strip() for line in open("./users", 'r')]
numUser=1
for username in usernameData:
    global usernameC
    generateOverview(username)
    repoNumG=repoNumG/25.0;
    generateRepo(username)
    usernameC.append(username)
    print username + " " +str(numUser)
    numUser=numUser+1
    
    print "**********"

    
df=DataFrame({'Username':usernameC,'Repositories':repoNumC,'Forked':forkedReposC,'Starred':starNumC,
             'Followers':followerNumC,'Following':followingNumC,'Company':orgNameC,
             'Location':locationNameC,'MailID':mailIdC,'Website':webUrlC,
             'Bio':bioC,'Orgnisations':orgListC,'Years_Active':yearsActiveC,
             'Pinned_Repos':pinnedRepoC,'Languages':repoLanguagesC})

df = df[['Username','Repositories','Forked','Starred',
             'Followers','Following','Company',
             'Location','MailID','Website',
             'Bio','Orgnisations','Years_Active',
             'Pinned_Repos','Languages']]

df.to_excel('GitHub_Data.xlsx', sheet_name='sheet1', index=False)