from interface import admin_interface as admin
from lib import common
user_info={}
def register():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        confirm_password=input('请确认密码：').strip()
        if password==confirm_password:
            #调用接口层
            flag,msg=admin.admin_register_interface(username, password)
            if flag==False:
                print(msg)
                continue
            else:
                print(msg)
                break
        else:
            continue

def login():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        #调用接口层
        flag,msg=admin.admin_login_interface(username,password)
        if flag:
            print(msg)
            user_info['user']=username
            break
        else:
            print(msg)
            continue

@common.auth(role='admin')
def create_school():
    while True:
        school_name=input('请输入学校名称：').strip()
        school_addr=input('请输入学校地址：').strip()
        #调用接口层
        flag,msg=admin.create_school_interface(school_name,school_addr,user_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue

    

@common.auth(role='admin')
def create_course():
    pass

@common.auth(role='admin')
def create_teacher():
    pass


func_dict={
    "1":register,
    "2":login,
    "3":create_school,
    "4":create_course,
    "5":create_teacher
}
def admin_view():
    while True:
        print('''
        1. 注册
        2. 登陆
        3. 创建学校
        4. 创建课程
        5. 创建老师
        ''')
        choice=input('请选择功能编号：').strip()
        if choice not in func_dict:
            print('输入错误，请重新输入！')
            continue
        func_dict.get(choice)()
