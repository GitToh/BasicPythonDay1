import pymysql.cursors
from Utils import*


conn = Utils.conndb.getConn()

try:
    cursor = conn.cursor()
    # SQL
    sql = 'SELECT * FROM employee'
    cursor.execute(sql)

    # Loop
    for r in cursor:
        print(r)

except pymysql.Error as e:
    print('Error %s' % e.args[1])

finally:
    # ปิด connection
    conn.close()
