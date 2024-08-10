from lib import common
from interface import teacher_interface

teacher_info={}

def login():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        flag,msg=teacher_interface.teacher_login_interface(username,password)
        if flag:
            print(msg)
            teacher_info['user']=username
            break
        else:
            print(msg)
            continue


@common.auth(role='teacher')
def check_courses():
    pass

@common.auth(role='teacher')
def choose_course():
    pass

@common.auth(role='teacher')
def check_students():
    pass   

@common.auth(role='teacher')
def modify_score():
    pass


func_dict={
    "1":login,
    "2":check_courses,
    "3":choose_course,
    "4":check_students,
    "5":modify_score
}
def teacher_view():
    while True:
        print('''
        1. 登陆
        2. 查看教授课程
        3. 选择教授课程
        4. 查看课程下的学生
        5. 修改学生成绩
        ''')

        choice=input('请选择功能编号：').strip()
        if choice not in func_dict:
            print('输入错误，请重新输入！')
            continue
        func_dict.get(choice)()