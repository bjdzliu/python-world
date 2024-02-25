import  pymysql
conn=None
db_params = {
    'host': '47.92.245.59',
    'user': 'root',
    'password': 'liudz133',
    'database': 'classicmodels',
}
try:
    conn=pymysql.connect(**db_params)
    print(conn.ping(False))
    cursor=conn.cursor()
    sql="select * from customers where customerNumber in (103,131,128,129,141) "

    rows=cursor.execute(sql)
    #获取一行
    results=cursor.fetchone()
    results=cursor.fetchmany(2)

    #把剩余的都获取
    results=cursor.fetchall()

    #重置游标，到第一行
    cursor.rownumber=1
    results=cursor.fetchall()
    #print(len(results))
    for i in range(len(results)):
        print(results[i])
        print("name is ",results[i][1])

    cursor.close()
    conn.commit()

except:
    conn.rollback()
finally:
    if conn:
        conn.close()