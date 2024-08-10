from db import models
def admin_register_interface(username, password):
    #1. 判断用户是否存在
    user_obj=models.Admin.select(username)
    if user_obj:
        return False,"对象已存在"

    #2.新用户创建
    admin_obj=models.Admin(username, password)
    admin_obj.save()
    return True,"用户创建成功"

def admin_login_interface(username,password):
    #1.判断用户是否存在
    user_obj=models.Admin.select(username)
    if not user_obj:
        return False,"用户不存在"

    #2.判断密码是否正确
    if password==user_obj.pwd:

        return True,"登陆成功"
    else:
        return False,"密码错误"
def create_school_interface(school_name,school_addr,admin_name):
    #1.判断学校是否存在
    school_obj=models.School.select(school_name)
    if school_obj:
        return False,"学校已存在"
    #2.创建学校

    admin_obj=models.Admin.select(admin_name)
    flag=admin_obj.create_school(school_name,school_addr)
    return True,f"{school_name} 学校创建成功"


