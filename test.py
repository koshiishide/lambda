import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', db='mysql')

try:
    with conn.cursor() as cursor:
        sql = "show databases;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()