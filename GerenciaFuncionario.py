import sqlite3

conexao = sqlite3.connect('funcionarios.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Funcionarios(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cargo TEXT NOT NULL,
salario DECIMAL(10, 2))"""
)

funcionarios = [
    ('Ryan', 'Programador', 130000),
    ('Roberto', 'Programador', 1300),
    ('Flajola', "Desenvolvedor", 500),
    ('Ricardo', 'Maquinario', 100),
    ('Walter', 'Cozinheiro', 500)
]

cursor.executemany('INSERT INTO Funcionarios(nome, cargo, salario) VALUES (?,?,?)', funcionarios)

conexao.commit()




# for funcionario in lista_de_funcionario:
  #  print(f"{funcionario[1]: <10} {funcionario[2]: <15} {funcionario[3]: <20}")

def add_funcionario():
    nome = input("Digite o nome: ")
    cargo = input("Digite o cargo: ")
    salario = input("Digite o salário: ")

    novo_funcionario = [nome, cargo, salario]
    inserir_funcionario = "INSERT INTO Funcionarios(nome, cargo, salario) VALUES (?,?,?)"
    cursor.execute(inserir_funcionario, novo_funcionario)
    conexao.commit()

def remover_funcionario():
    funcionario_nome = input("Digite o nome do funcionario: ")

    excluir_funcionario = "DELETE FROM Funcionarios WHERE nome = ?"
    cursor.execute( exclui_funcionario, (funcionario_nome))
    conexao.commit()

def view_funcionarios():
    cursor.execute('SELECT * FROM Funcionarios')
    lista_de_funcionario = cursor.fetchall()

    print(f"{'NOME':<10} {'CARGO':<15} {'SALARIO':<20}")
    for funcionario in lista_de_funcionario:
        print(f"{funcionario[1]: <10} {funcionario[2]: <15} {funcionario[3]: <20}")

def atualizar_funcionario():
    while True:
        atualizar = input(
            "O que quer atualizar? Digite 'cargo' para atualizar o Cargo ou 'salario' para atualizar o Salario:"
            " ").lower()
        if atualizar == 'cargo':
            nome = input("Digite o nome: ")
            novo_cargo = input("Digite o novo cargo: ").lower()
            tualizar_funcao = "UPDATE Funcionarios SET cargo = ? WHERE nome = ?"
            cursor.execute( tualizar_funcao, (novo_cargo, nome))
            break
        elif atualizar == 'salario':
            nome2 = input("Digite o nome: ")
            novo_salario = input("Digite o novo salario: ").lower()
            atualizar_funcao = "UPDATE Funcionarios SET salario = ? WHERE nome = ?"
            cursor.execute( atualizar_funcao, (novo_salario, nome2))
            break
        else:
            print("Por favor, digite um elemento válido")
    conexao.commit()

atualizar_funcionario()
conexao.close()