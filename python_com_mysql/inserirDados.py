from connection import conectaDb

# Obter uma conexao com o banco de dados
conn = conectaDb('localhost', 'root', '123456', 'pessoas')

# recupera o cursor
c = conn.cursor()

# define um lista de pessoas
listaPessoas  = [('Jones Quito') ,('Simone Cardoso') ,('Fernanda Chaves') ,
                 ('Maria Antonia') ,('Telma Leitão')]


# define um lista de telefones
listaTelefones = [('1', '99626-4766'),('1', '99109-2460'),('4', '99109-2125'),
                  ('3', '99205-4288'),('5', '99300-1500'),('5', '99303-9783')]


# insere dados na tabela de pessoas
c.executemany("insert into pessoas (nome) values (%s)", listaPessoas)

# insere dados na tabela de telefones
c.executemany("insert into telefones (pessoa_id, fone) values (%s, %s)", listaTelefones)

conn.commit()
conn.close()



