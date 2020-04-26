import pymysql.cursors
from Utils import*


conn = Utils.conndb.getConn()

try:
    cursor = conn.cursor()
    # SQL
    sql = 'INSERT INTO employee (no, name, salary) VALUES (%s, %s, %s)'

    # Execute sql and pass 3 parameter
    cursor.execute(sql, ('1', 'Samit', '20000'))
    conn.commit()

    print('Create new employee success')

except pymysql.Error as e:
    print('Error %s' % e.args[1])

finally:
    # ปิด connection
    conn.close()
