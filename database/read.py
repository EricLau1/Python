# download puglin mysql -> pip install PyMySQL

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')

myCursor = conn.cursor()

def find(id, cursor):

    cursor.execute("select * from produto where id = %s", (id))

    data = cursor.fetchone()

    return data

#END find

def getAll(table, cursor):

    sql = "select * from " + table

    cursor.execute(sql);

    results = cursor.fetchall()

    return results
#END getAll

busca = find(3, myCursor) 

dados = getAll('produto', myCursor)

print("====== BUSCA ======")
print(busca)

print("\n\n")
print("====== TODOS ======")

for produto in dados:
    print(produto)

conn.close()