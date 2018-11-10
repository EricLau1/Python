# download puglin mysql -> pip install pymysql

import pymysql

data = [
    { 'id' : 1, 'descricao' : 'Laranja', 'valor' : 2.57, 'quantidade' : 45 },
    { 'id' : 2, 'descricao' : 'Banana', 'valor' : 5.89, 'quantidade' : 100 },
    { 'id' : 3, 'descricao' : 'Morango', 'valor' : 10.45, 'quantidade' : 500 }
]

conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')

myCursor = conn.cursor()

def create(produto, cursor):

    sql = "insert into produto (descricao, valor, quantidade) values ( %s, %s, %s )"

    result = cursor.execute(sql, (produto['descricao'], produto['valor'], produto['quantidade']))

    print(result)
#END create

create(data[2], myCursor)

conn.commit()

conn.close()

