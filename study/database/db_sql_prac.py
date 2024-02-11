#!/usr/bin/python3
"""
create database use flask_sql_demo;
use flask_sql_demo;
create table entityname(name varchar(100),entityid varchar(100));
insert into entityname values("alibaba","abdj23j");

"""

import pymysql,json

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="liudz133", database="flask_sql_demo")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


name="ali"
# SQL 插入语句
sql = "select  * from entityname where name like '%s%%'" % (name)

try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    msg={}
    for row in results:
        msg['entityname']=row[0]
        msg['entityid']=row[1]
    # 提交到数据库执行
    db.commit()
    jsonstr=json.dumps(msg)
    print(jsonstr)
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()