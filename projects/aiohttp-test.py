from aiohttp import web

#hello world;  method: GET ; PATH: /
async def hello(request):
    return web.Response(text="hello world")

# method: GET   PATH: /myresponse
async def mygetresponse(request):
    for k,v in dict(**request.match_info):
        print(k,v)
    return web.Response(text="this is my response for /myresponse")

#method : POST  PATH: /mypost
async def post_handler(request):
    params = await request.post()
    print(type(request.match_info))
    for k,v in dict(**request.match_info):
        print(k,v)
    print("params.items()",params.items())
    for k,v in params.items():
        print(k,v)
    return web.Response(text="this is for pot method")

app = web.Application()
resource = app.router.add_resource('/path2', name='name')
route = resource.add_route('GET', mygetresponse)

app.router.add_get('/',hello)
app.router.add_get('/myresponse', mygetresponse)
app.router.add_route('POST', '/mypost', post_handler)

#### for other get method
async def variable_handler(request):
    print('itme:',request.match_info.items())
    for k,v in request.match_info.items():
        print(k,v)
    return web.Response(
       text="Hello, {}".format(request.match_info['name']))
resource = app.router.add_resource('/all/{name}')
resource.add_route('GET', variable_handler)
app['__file1__'] = "mytest"
app['__file2__'] = "mytest2"
print(app.__getitem__('__file1__'))
print(app.__len__())
print(app['__file1__'] )
from collections import Iterable
print(isinstance(app , Iterable))
web.run_app(app)

#jinjia2模板
app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('/path/to/templates/folder'))