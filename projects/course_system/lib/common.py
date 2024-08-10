def auth(role):
    from core import admin,student,teacher
    def login_auth(func):
        def inner(*args,**kwargs):
            if role=='admin':
                if not admin.user_info.get('user'):
                    admin.login()
                else:
                    res=func(*args,**kwargs)
                    return res
            elif role=='student':
                if not student.user_info.get('user'):
                    student.login()
                else:
                    res=func(*args,**kwargs)
                    return  res
            elif role=='teacher':
                if not teacher.user_info.get('user'):
                    teacher.login()
                else:
                    res=func(*args,**kwargs)
                    return res
            else:
                #只能让admin，student，teacher三者来用装饰器
                print('当前视图层没有权限')
        return inner
    return login_auth