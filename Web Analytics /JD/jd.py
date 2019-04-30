#coding: utf-8

#import packages
import urllib2
import json


#the url you wanna crawl
url1='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv17182&productId=968093&score=0&sortType=5&page='
url2='&pageSize=10&isShadowSku=0&fold=1'

# create an empty list to store comments
comments=[]
for i in range(0,10): #the number of pages you wanna crawl
    url=url1+str(i)+url2
   
    print "Crawling page" + str(i+1)
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    html =response.read().decode('GBK')

    #remove redundant characters 
    html=html.replace('fetchJSON_comment98vv17182(','').replace(');','')
    b=json.loads(html)
    
    for k in b['comments']:
        content = k["content"].encode('utf-8')
        comments.append(content)

print len(comments)

#store review into a txt file 
with open('JD.txt','a') as f:
    for each in comments:
         f.write(each+'\n')  

