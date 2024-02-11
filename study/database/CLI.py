"""
###  添加
In [2]: from study.database.db_prac import *

role=Role(name='admin')

In [3]: role=Role(name='admin6',id=6)

In [4]: user=User(name='jack',role_id=role.id)

In [5]: db.session.add(user)

In [6]: db.session.add(role)

In [7]: db.session.commit()

###   添加多个信息
db.session.add_all([user1,user2])

# rollback
db.session.rollback()

### 修改

In [8]: user.name='chengxuyuan'

In [9]: db.session.commit()

### 删除

In [10]: db.session.delete(user)

In [11]: db.session.commit()


### 查询
User.query.all()

User.query.filter_by(id=3).all()

User.query.filter(User.id==3).all()

"""
