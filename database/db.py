# download puglin mysql -> pip install PyMySQL

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')

myCursor = conn.cursor()

# se a tabela ja existir ocorrerá um erro
myCursor.execute("""
create table if not produto(
id int auto_increment primary key,
descricao varchar(50) not null,
valor double not null,
quantidade int
);
""")

conn.commit()

conn.close()
