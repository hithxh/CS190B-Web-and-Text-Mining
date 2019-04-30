#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk
import jieba
from nltk import FreqDist
import jieba.posseg as pseg 

#read file from local 
f = open('JD.txt','r')
raw = f.read()

#generate tokens by jieba
tokens = pseg.cut(raw)

#load chinese stop words
stopword=[]
cfp=open('stopwords.txt','r+')  
for line in cfp:
    for word in line.split():
        stopword.append(word)
cfp.close()

# remove characters in chinese stop words
wordlist_N = []
for t in tokens:
    if t.word not in stopword:
        if t.word != '\n'  and t.word != '―' and t.word!=' ' and t.word!='\u200b' and t.word!='\n' and t.word!='##' and t.flag.startswith('n'):
            wordlist_N.append(t)

#generate a frequency dictionary for wordlist_N
freq = FreqDist(wordlist_N)

#sort the frequency list in descending order
sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)

#write result into .txt file
with open ('7.cn_POS_Tagging.txt','w+') as f:
    for line in sorted_freq:
        f.write(str(line[0].word)+'\t'+str(line[0].flag)+'\t'+str(line[1])+'\n')
