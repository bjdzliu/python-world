import config_default


class Dict(dict):
    def __init__(self,name=(),values=(),**kw):
        super(Dict,self).__init__(**kw)
        for k,v in zip(names,values):
            self[k]=v
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        def __setattr__(self, key, value):
            self[key]=value


import config_override.configs

def test():
    for k in config_override:
        print(k)

test()


