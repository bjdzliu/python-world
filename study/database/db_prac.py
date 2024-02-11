from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql,time

#pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:liudz133@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

"""
两张表
user：外键
role:name ; id 主键
"""


class Role(db.Model):
    #定义table
    __tablename__="roles"
    #定义字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

    # role:users 1:n 写一个关联
    # user 使用 backref='Role'，定义在Role中，user.role 可以用
    users = db.relationship('User',backref='role')


class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16))
    email=db.Column(db.String(32),unique=True)
    password=db.Column(db.String(32))
    # 定义外键的方式
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    #User 希望有role属性，这个定义，再另一个模型，role中去做。

    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name,self.id,self.email,self.password)


"""
自定义一个log表
"""

class Logs(db.Model):
    __tablename__="myloginlog"
    id=db.Column(db.Integer,primary_key=True)
    entry=db.Column(db.String(32),unique=False)

"""
flask_sqlalchemy需要一个叫id的列，作为pk。
自定义列名作为pk
"""
class Logs2(db.Model):
    __tablename__="myloginlog2"
    #id=db.Column(db.Integer,primary_key=True)
    myselfid=db.Column(db.Integer)
    entry=db.Column(db.String(32),unique=False)
    __mapper_args__ = {
        'primary_key': [myselfid]
    }

@app.route('/')
def index():
    return 'Hello World'

if __name__=='__main__':
    #app.run(debug=True)
    #db.drop_all()
    db.create_all()
    logentry=Logs(entry=time.strftime("%Y%m%d %X", time.localtime()))
    db.session.add(logentry)
    db.session.commit()
    app.run()



"""
enter ipython3
from study.database.db_prac import *
"""



