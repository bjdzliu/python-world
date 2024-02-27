

import re
import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# myssl = ssl.create_default_context();
# myssl.check_hostname=False
# myssl.verify_mode=ssl.CERT_NONE

def getHtml(url):
    with urllib.request.urlopen(url) as response:
       
        html = response.read().decode( response.headers.get_content_charset())
    return html
 
def getImg(html):
    print(html)
    reg= r'src="(.*?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

x=0
html = getHtml("https://pic.yesky.com/c/6_25152.shtml")  # 使用你的URL替换 "http://www.example.com"
for imgurl in getImg(html):
   #保存文件到本地路径
   urllib.request.urlretrieve(imgurl, '%s.png' % x)
   x += 1
print(f"一共有 {x} 个png图片")