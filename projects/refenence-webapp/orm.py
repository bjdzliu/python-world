#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio,logging
import aiomysql

def log(sql,args=()):
    logging.info('SQL:%s' % sql)

async def create_pool(loop,**kw):
    logging.info('create database pool ...')
    global __pool
        __pool = await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get['charset','utf8'],
        autocommit=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

async def execute(sql,args,autocommit=True):
    log(sql)
    #建立db连接
    async with __pool.get() as conn:
        if not autocommit:
            #if不自动提交,开始事务A
            await conn.begin()
        try:
            #游标返回值类型为字典
            async with conn.cursor(aiomysql.DictCursor) as cur:
             #执行sql语句
                await cur.execute(sql.replace('?','%s'),args or ())
             #rowcount
                affected = cur.rowcount
             # if不自动提交,事务A提交
             if not autocommit:
                 await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise  #手动抛出异常
        return affected

async def select(sql,args,size=None):
    log(log,args)
    global __pool
    aysnc with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs=await cur.fetchmany(size)
            else:
                rs = await cur.fetchll()
        logging.info('row return :%s' % len(rs))
        return rs

class ModelMetaclass(type):


#多重继承,元类是ModelMetaclass
class Model(dict, metaclass=ModelMetaclass):
#调用父类的init方法
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        expect KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value

    def getValue(self,  key):
        return getattr(self,key,None)

    def getValueOrDefult(self,key):
        value = getattr(self,key,None)
        if value is None:
            filed = self.__mappings__[key]
            if filed.default is not None:
                #callable()判断对象是否调用
                value=filed.default() if callable(filed.default) else field.default
                logging.debug('using default value for %s:%s' % (key,str(value)))
                setattr(self,key,value)
        return value





