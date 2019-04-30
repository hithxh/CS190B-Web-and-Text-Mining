#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from weibo import APIClient
import webbrowser  # python内置的包

APP_KEY = 4048500746  # 你的app_key
APP_SECRET = 'd3b6ec487641d5d46a3aee693106718c'  # 你的app_secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # 网站回调地址

# 在网站设置"使用微博账号登陆"的链接，当用户点击链接后，引导用户跳转至如下地址
# 利用官方微博ADK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
# 得到授权页面的url，利用webbrowser打开这个url
url = client.get_authorize_url()
print url
webbrowser.open_new(url)   # 打开了一个网址，网址后面附带了你需要的code

# 用户授权后，将跳转至网站回调地址，并附加参数code=abcd1234

# 获取URL参数code：
print "输入url中code后面的内容后按回车键："
code = raw_input()   # 人工输入网址后面的code内容


r = client.request_access_token(code)  # 获得用户授权

# 保存access_token, expires_in
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in
# 设置得到的access_token，client可以直接调用API了
client.set_access_token(access_token, expires_in)

# 

statuses = client.statuses__friends_timeline()['statuses']
length = len(statuses)
print length
# 输出信息
stas1=[]
stas2=[]
stas3=[]
stas4=[]
stas5=[]
for i in range(0, length):
    print u"微博创建时间:" + statuses[i]['created_at']
    print u'昵称:' + statuses[i]['user']['screen_name']
    print u'简介:' + statuses[i]['user']['description']
    print u'位置:' + statuses[i]['user']['location']
    print u'微博:' + statuses[i]['text']
    stas1.append(statuses[i]['created_at'])
    stas2.append(statuses[i]['user']['screen_name'])
    stas3.append(statuses[i]['user']['description'])
    stas4.append(statuses[i]['user']['location'])
    stas5.append(statuses[i]['text'])

with open('Weibo.txt','a') as f:
    for i in range(length):
        f.write(u"微博创建时间:" + stas1[i]+'\n')
        f.write(u'昵称:' +stas2[i]+'\n')
        f.write(u'简介:' +stas3[i]+'\n')
        f.write(u'位置:' +stas4[i]+'\n')
        f.write(u'微博:' +stas5[i]+'\n')

