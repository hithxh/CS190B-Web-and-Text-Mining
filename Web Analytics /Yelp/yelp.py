
# coding: utf-8
# BeautifulSoup Demo

#import packages
from bs4 import BeautifulSoup
import urllib2

#the url you want crawl
url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'

#use urllib2 module to open the url 
ourUrl=urllib2.urlopen(url)

soup=BeautifulSoup(ourUrl,'html.parser')
#create a BeautifulSoup object, which represents the document as a nested data structure
#parse the page 

# to see what inside the soup 
# print soup.prettify()

review=[]  # create an empty list to store reviews 
for i in soup.find_all('div',{'class':'review-content'}):  
    per_review=i.find('p')  # extract review
    print per_review
    review.append(per_review)  # append review

len(review)  # how many reviews we collect 

####basic clean 
New_review=[]  # create an empty list to store new reviews
for each in review:
    new_each=str(each).replace('<br/>','') #remove html tags 
    new_each=new_each[13:-4]
    #print new_each
    New_review.append(new_each)
#len('<p lang="en">)
#len('</p>')

#store review into a txt file 
with open('Yelp.txt','a') as f:
    for each in New_review:
         f.write(each+'\n')  # easily open with notepad+++

