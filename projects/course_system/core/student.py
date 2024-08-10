from lib import common
from interface import student_interface

student_info={}

def register():
    print('学生注册')
def login():
    print('学生登陆')

@common.auth(role='student')
def choose_school():
    print('选择校区')

@common.auth(role='student')
def choose_course():
    print('选择课程')

@common.auth(role='student')
def check_score():
    print('查看分数')


func_dict={
    "1":register,
    "2":login,
    "3":choose_school,
    "4":choose_course,
    "5":check_score
}
def student_view():
    while True:
        print('''
        1. 注册
        2. 登陆
        3. 选择校区
        4. 选择课程
        5. 查看分数
        ''')
        choice=input('请选择功能编号：').strip()
        if choice not in func_dict:
            print('输入错误，请重新输入！')
            continue
        func_dict.get(choice)()