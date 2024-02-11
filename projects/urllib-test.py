from urllib.parse import urlparse
from urllib.parse import parse_qs
print(dir(urlparse))
url='http://www.baidu.com/index.php?username=guol&param2=4'
def qs(url):
    query = urlparse(url).query
    print(parse_qs(query))  #{'username': ['guol'], 'param2': ['4']}
    print('items:',parse_qs(query).items()) #dict_items([('username', ['guol']), ('param2', ['4'])])
    return dict([(k,v[0]) for k,v in parse_qs(query).items()])
print(qs(url))

for k,v in [(1,"1"),(2,"2")]:
    print(k,v)

string="aa"
for k,v in parse_qs(string).items():
    print('k is ',k)
