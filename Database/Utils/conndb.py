import pymysql.cursors


# Function connect db and returnconnection
def getConn():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='1234',
                           db='pythontestdb',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


print(getConn())
