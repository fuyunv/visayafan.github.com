"""
将微博网页保存下来后用此脚本进行转换
效果：http://visayafan.com/others/log/weibo.html
"""

from time import strptime, strftime

from bs4 import BeautifulSoup


pre = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN" xml:lang="zh-CN">
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <meta name="generator" content="Org-mode"/>
    <meta name="author" content="visayafan"/>
    <link rel="stylesheet" type="text/css" href="../../layout/css/bootstrap_old.css" />
    <link rel="stylesheet" type="text/css" href="../../layout/css/style.css" />
    <script src="../../layout/js/jquery_1.7.1.js"></script>
    <script src="../../layout/js/bootstrap_old.js"></script>
    <style type="text/css">
        code{
            background-color:transparent;
            border:none;
        }
        .DateModified {
       	    direction: ltr;
       	    line-height: 1.15;
       	    text-indent: 0pt;
       	    font-size: 8pt;
       	    text-align: right;
       	    font-family: Arial;
       	    color: gray;
        }
    </style>
  </head>
  <body>
    <div id="content">
      <h1 class="title"></h1>
      '''

post = ''' </div> </body></html>'''

datePre = '<p class="DateModified">'
datePost = '</p><hr></hr>'

soup = BeautifulSoup(open("/Users/visayafan/tmp/weibo/weibo.html", 'r'))
weibos = soup.find_all('div', attrs={'class': 'WB_text W_f14'})
dates = soup.find_all('a', attrs={'class': "S_txt2", 'node-type': "feed_list_item_date"})
weibofile = open('/Users/visayafan/visayafan.github.com/others/log/weibo.html', 'w')
content = '<hr>'
for (w, d) in zip(weibos, dates):
    content += str(w)
    content += strftime('%Y年%m月%d日 %H:%M', strptime(d['title'], "%Y-%m-%d %H:%M"))
weibofile.write(BeautifulSoup(pre + content + post).prettify())
weibofile.close()