import sqlite3

conexao = sqlite3.connect('banco_de_dados')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id
# (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
# exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Thaís", 23, "Engenharia Biomédica");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Roseli", 53, "Engenharia Elétrica");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Sérgio", 54, "Engenharia de Automação");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Alcione", 30, "Moda");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Reginaldo", 23, "Medicina");')

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".

alunos = cursor.execute('SELECT * FROM alunos')

for aluno in alunos:
   print(aluno)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

alunos_mais_de_vinte = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

for aluno in alunos_mais_de_vinte:
  print(aluno)
    
# c) Selecionar os alunos do curso de "Engenharia" em ordem
# alfabética.

alunos_engenharia_ordenados = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "Engenharia%" ORDER BY nome ASC')

for aluno in alunos_engenharia_ordenados:
   print(aluno)
    
# d) Contar o número total de alunos na tabela

total = cursor.execute('SELECT COUNT(*) FROM alunos')

for total_alunos in total:
  print(total_alunos)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade=20 WHERE nome = "Alcione"')

# b) Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id = "1"')

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Thaís", 23, 1500.50);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Renata", 60, 180.38);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Sérgio", 45, 10000000);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Roseli", 23, 20000000);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Tamires", 23, 45.70);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, "Vinicius", 23, 1.30);')

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a
# 30 anos.

clientes_idade_maior_30 =cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')

for cliente in clientes_idade_maior_30:
    print(cliente)

# b) Calcule o saldo médio dos clientes.

saldo_medio_clientes = cursor.execute('SELECT AVG(saldo) FROM clientes').fetchone()[0]
print(saldo_medio_clientes)

# c) Encontre o cliente com o saldo máximo.

cliente_saldo_max = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC').fetchone()[0]
print(cliente_saldo_max)

# d) Conte quantos clientes têm saldo acima de 1000.

clientes_saldo_maior_1000 =cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000').fetchone()[0]
print(clientes_saldo_maior_1000)

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo=2000 WHERE nome="Renata"')

# b) Remova um cliente pelo seu ID.

cursor.execute('DELETE FROM clientes WHERE id=5')

# 8. Junção de Tabelas

# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real).

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY,cliente_id INT, produto VARCHAR(50), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".

cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1, 1,"abacaxi", 3)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2, 2,"macarrão", 4.5)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3, 3,"panela", 39.99)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4, 4,"sorvete", 25.5)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.

consulta = cursor.execute('SELECT nome, produto, valor FROM clientes cl JOIN compras co ON cl.id=co.cliente_id')

for cliente in consulta:
  print(cliente)

conexao.commit()
conexao.close