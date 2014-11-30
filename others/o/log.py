from time import strptime, strftime
from shutil import rmtree, copytree
import os

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
imagePre = '<center> <a class="lightbox" href="'
imageMid = '"> <img class="lightbox " title="点击查看大图" src="'
imagePost = '" height="200"> </a> </center>'
imageFluidPre = '<div class="row-fluid">'
imageFluidPost = '</div>'
imageSpanPre = '<div class="span'
imageSpanPre2 = '">'
imageSpanPost = '</div>'
datePre = '<p class="DateModified">'
datePost = '</p><hr></hr>'


def composeImageStr(imagePaths):
    imageStr = ''
    # if len(imagePaths) == 1:
    # imageStr = imagePre + imagePaths[0] + imageMid + imagePaths[0] + imagePost
    if len(imagePaths) in [1, 2, 3]:
        imageStr += imageFluidPre
        for imagePath in imagePaths:
            imageStr += imageSpanPre + str(int(12 / len(
                imagePaths))) + imageSpanPre2 + imagePre + imagePath + imageMid + imagePath + imagePost + imageSpanPost
        imageStr += imageFluidPost
    elif len(imagePaths) == 4:
        imageStr += imageFluidPre
        for i in range(2):
            imageStr += imageSpanPre + str(6) + imageSpanPre2
            for j in range(2):
                imageStr += imagePre + imagePaths[2 * i + j] + imageMid + imagePaths[2 * i + j] + imagePost
            imageStr += imageSpanPost
        imageStr += imageFluidPost
    return imageStr


def composeDateStr(dateStr):
    convertedDateStr = strftime('%Y年%m月%d日 %H:%M', strptime(str(dateStr.next).rstrip(),
                                                            "%A, %B %d, %Y at %I:%M %p"))
    return datePre + convertedDateStr + datePost


srcPrefix = '/Users/visayafan/tmp'
dstPrefix = '/Users/visayafan/visayafan.github.com/others/log'
memoriesHtml = 'memories.html' if os.path.isfile(os.path.join(srcPrefix, 'memories.html')) else 'memories/memories.html'

soup = BeautifulSoup(open(os.path.join(srcPrefix, memoriesHtml), 'r'))
logfile = open(os.path.join(dstPrefix, 'log.html'), 'w')

content = '<hr>'
logs = soup.find_all('p', dir='ltr')
dates = soup.find_all('p', attrs={'class': 'sDateCreated'})
for (log, date) in reversed(list(zip(logs, dates))):
    content += str(log)
    if memoriesHtml != 'memories.html':
        imageLog = log.find_next('p').find_next('p')
        imagePaths = []
        while imageLog.has_attr('class') and imageLog['class'] == ['imgPara']:
            imagePaths.append(imageLog.find_next('img')['src'])
            imageLog = imageLog.find_next('p')
        if imagePaths:
            rmtree(os.path.join(dstPrefix, 'images'), ignore_errors=True)
            copytree(os.path.join(srcPrefix, 'memories/images'), os.path.join(dstPrefix, 'images'))
            content += composeImageStr(imagePaths)
    content += composeDateStr(date)
logfile.write(BeautifulSoup(pre + content + post).prettify())
logfile.close()
rmtree(os.path.join(dstPrefix, 'memories.zip'), ignore_errors=True)
os.remove(os.path.join(srcPrefix, 'memories.html')) if memoriesHtml=='memories.html' else rmtree(os.path.join(srcPrefix, 'memories'), ignore_errors=True)