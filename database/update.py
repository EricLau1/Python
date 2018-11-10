# download puglin mysql -> pip install pymysql

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')

myCursor = conn.cursor()

def atualizar(produto, cursor):

    sql = " update produto set descricao = %s, valor = %s, quantidade = %s where id = %s";

    result = cursor.execute(sql, (produto['descricao'], produto['valor'], produto['quantidade'], produto['id']))

    print(result)
#END create

data = { "id" : 7, "descricao" : "Café", "valor" : 9.90, "quantidade" : 20 }

atualizar(data, myCursor)

conn.commit()

conn.close()

