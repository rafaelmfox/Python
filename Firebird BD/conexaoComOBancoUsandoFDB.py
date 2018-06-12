
#importar a biblioteca
import fdb

#conexao local
#con = fdb.connect(dsn='C:/BD.FBD', user='sysdba', password='masterkey')

#conexao por nome de rede
con = fdb.connect(dsn='nomeMicro:/BD.FBD', user='sysdba', password='masterkey')

#exeplo conexao por Ip
#con = fdb.connect(dsn='192.168.0.1:/BD.FBD', user='sysdba', password='masterkey')

#Leitor
cur = con.cursor()

#bom e velho select
cur.execute("select a.nome from tabela a")

#mostra tudo sem formatação
print (cur.fetchall())

#fecha conexao
con.close()














