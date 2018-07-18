from connection import conectaDb

# Obter uma conexao com o banco de dados
conn = conectaDb('localhost', 'root', '123456', 'pessoas')

if(conn == 0): exit(0)

# recupera o cursor
c = conn.cursor()

# cria a tabela de pessoas
c.execute('create table if not exists pessoas(id integer auto_increment primary key,'+
				'nome varchar(20)not null)')

# cria a tabela de telefones
c.execute('create table if not exists telefones(pessoa_id integer not null,'+
				'fone varchar(20)not null)')


conn.commit()
conn.close()
