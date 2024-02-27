
#在python3.3后urllib2已经不能再用，只能用urllib.request来代替
"""
python 3.x中urllib库和urilib2库合并成了urllib库。。
其中    urllib2.urlopen()变成了urllib.request.urlopen()
       urllib2.Request()变成了urllib.request.Request()

"""

from urllib import request
import urllib

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# with request.urlopen('https://www.baidu.com') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))


#### 加入头信息的方式
req = request.Request(url='http://www.douban.com/',headers={})

req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    #<class 'http.client.HTTPResponse'>
    print(type(f))
    for k, v in f.getheaders():
        print('getheaders content ### %s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))





### azure GET
headers = {"Content-Type": "application/json"}
params = urllib.parse.urlencode({'api-version': '2018-09-01'})
url= "https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets?%s" % params
#if use “data” in Request, it's POST
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))


### POST
