import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk
import jieba
from nltk import FreqDist

#read file from local 
f = open('JD.txt','r')
raw = f.read()

#generate tokens by jieba
tokens = jieba.lcut(raw)

#generate a frequency dictionary for all tokens
freq = FreqDist(tokens)

#sort the frequency list in descending order
sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)

#write result into .txt file
with open ('5.cn_frequency.txt','w+') as f:
    for line in sorted_freq:
        f.write(str(line[0])+'\t'+str(line[1])+'\n')

