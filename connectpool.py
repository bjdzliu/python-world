import asyncio
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test_example():
    conn = yield from aiomysql.connect(host='192.168.56.6', port=3306,
                                       user='root', password='passw0rd',
                                       db='mysql', loop=loop)

    # create default cursor
    cursor = yield from conn.cursor()

    # execute sql query
    yield from cursor.execute("SELECT Host, User FROM user")

    # fetch all results
    r = yield from cursor.fetchone()
    print(r)
    # detach cursor from connection
    yield from cursor.close()
    a=None
    print (a or "2")
    # close connection
    conn.close()

loop.run_until_complete(test_example())