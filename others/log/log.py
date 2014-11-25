from bs4 import BeautifulSoup
from time import strftime,strptime
import sys
import os
from os.path import expanduser

pre ='''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN" xml:lang="zh-CN">
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <meta name="generator" content="Org-mode"/>
    <meta name="author" content="visayafan"/>
  </head>
  <body>
    <div id="content">
      <h1 class="title"></h1>
      <link rel="stylesheet" type="text/css" href="../../layout/css/bootstrap_old.css" />
      <link rel="stylesheet" type="text/css" href="../../layout/css/style.css" />
      <script src="../../layout/js/jquery_1.7.1.js"></script>
      <script src="../../layout/js/bootstrap_old.js"></script>
      '''

post='''  </body></html>'''

code = '<code>====================================================================</code>'

soup=BeautifulSoup(open(sys.argv[1], 'r'))
log=open(os.path.join(expanduser("~"),'visayafan.github.com/others/log/log.html'),'w')

ps=soup.find_all('p', dir='ltr')
ts=soup.find_all('p', attrs={'class':'sDateCreated'})

content=code
for (t,p) in zip(ts,ps):
    content+=str(p)
    # https://docs.python.org/2/library/time.html
    content += strftime('%Y年%m月%d日 %H:%M',strptime(str(t.next).rstrip(),"%A, %B %d, %Y at %I:%M %p"))
    content+='<br>'+code
log.write(BeautifulSoup(pre+content+post).prettify())
log.close()
