# download puglin mysql -> pip install pymysql

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')

myCursor = conn.cursor()

def deletar(id, cursor):

    sql = "delete from produto where id = %s";

    result = cursor.execute(sql, (id))

    print(result)
#END create

deletar(1, myCursor)

conn.commit()

conn.close()

