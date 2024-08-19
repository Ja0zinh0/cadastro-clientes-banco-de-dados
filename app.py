import sqlite3

conexao = sqlite3.connect('funcionarios.db')
cursor = conexao.cursor()
cursor.execute("""
 CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        dataContratacao TEXT NOT NULL 
    );

""")
conexao.commit()

nome = input('Digite o nome do funcionario: ')
cargo = input('Digite o cargo do funcionario: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')

cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)",(1,nome,cargo,data))
conexao.commit()

nome = input('Digite o nome do funcionario: ')
cargo = input('Digite o cargo do funcionario: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')

cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)",(2,nome,cargo,data))
conexao.commit()

conexao.close()