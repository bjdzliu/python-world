from db import models
def teacher_login_interface(username,password):
    #1.判断用户是否存在
    user_obj=models.Teacher.select(username)
    if not user_obj:
        return False,"用户不存在"

    #2.判断密码是否正确
    if password==user_obj.pwd:
        
        return True,"登陆成功"
    else:
        return False,"密码错误"