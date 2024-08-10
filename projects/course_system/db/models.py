from db import db_handler

class Base():
    def save(self):
        db_handler.save_data(self)
    @classmethod
    def select(cls,name):
        obj=db_handler.select_data(cls,name)
        return obj


class Admin(Base):
    def __init__(self,user, pwd):
        self.user = user
        self.pwd = pwd
    @classmethod
    def create_school(cls,school_name,school_addr):
        schoo_obj=School(school_name,school_addr)
        schoo_obj.save()
        return True
    
    @classmethod
    def create_course(cls,name):



class School(Base):
    def __init__(self,school_name,school_addr,user_name):
        self.user=school_name
        self.school_addr=school_addr
        self.create_course=user_name

class Teacher(Base):
    pass


class Student(Base):
    pass
    

class Course(Base):
    pass


