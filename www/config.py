import config_default
import sys
from collections import Iterable

print(sys.path)

class Dict(dict):
    def __init__(self,names=(),values=(),**kw):
        super(Dict,self).__init__(**kw)
        for k,v in zip(names, values):
            self[k]=v
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
            self[key]=value

def merge(defaults, override):
    r={}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k]=merge(v,override[k])
            else :
                r[k]=override[k]

        else:
            r[k] = v
    # for k,v in r.items():
    #     print('r',k,v)
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    # for k,v in D.items():
    #     if(k == "session") :
    #         print("session is k",v)
    #     else:
    #         print('DDDDDDD',k)
    return D

configs=config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
    # for k, v in configs.items():
    #     print(k,v)
except ImportError:
     pass

configs = toDict(configs)
print(configs['db'])



def get_configdefault():
    for k in config_override.configs:
        print("config_override.configs's key and value is ",k,config_override.configs[k])

#get_configdefault()


