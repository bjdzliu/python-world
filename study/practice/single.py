from functools import wraps

def singleton(cls):
    instances={}

    @wraps(cls)
    def wrappers(*args,**kwargs):
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return wrappers
@singleton
class Presideng:
    pass

