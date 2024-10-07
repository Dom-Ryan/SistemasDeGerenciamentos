import matplotlib.pyplot as plt
from prompt_toolkit.key_binding.bindings.search import abort_search


class Livro:
    def __init__(self, nome, autor, data, situacao):
        self.nome = nome
        self.autor = autor
        self.data = data
        self.situacao = situacao


    def status(self):
        return  (f"Nome: {self.nome};\n"
                f"Autor: {self.autor};\n"
                f"Data de Publicação:{self.data})\n"
                f"Situação: {self.situacao}")


livros = [  Livro('A Metamorfose', 'Franz Kafka', 1945, 'disponivel'),
            Livro('O Processo', "Franz Kafka", 1925, 'disponivel'),
            Livro('O Castelo', "Franz Kafka", 1926, 'emprestado'),
            Livro('A Muralha da China', "Franz Kafka", 1917, 'emprestado'),
            Livro("Amerika", 'Franz Kafka', 1927, 'disponivel'),
            Livro('Carta ao Pai', 'Franz Kafka', 1927, 'disponivel'),
            Livro("Na Colonia Penal", 'Franz Kafka', 1926, 'emprestado'),
            Livro("O Veredito", 'Franz Kafka', 1925, 'emprestado')
]

class Biblioteca:
    def __init__(self):
        self.livros = livros

    def add_livro(self, nome, autor, data, biblioteca=None):
         novo_livro = Livro(nome, autor, data, 'disponivel')
         biblioteca.append(novo_livro)
         return f"{nome} foi adicionado na Biblioteca"

    def listar_livros(self):
        return [livro.status() for livro in self.livros]

class Usuario:
    def __init__(self, nome, contato, em_posse=None):
        self.nome = nome
        self.contato = contato
        self.em_posse = em_posse if em_posse is not None else []

    def emprestar(self, livro):
        if livro.situacao == 'disponivel':
            livro.situacao = 'emprestado'
            self.em_posse.append(livro)
            print(f"{livro.nome} emprestado com sucesso!")
        else:
            print(f"{livro.nome} já esta emprestado")

    def devolver(self, livro):
       if livro in self.em_posse:
           livro.situacao = 'disponivel'
           self.em_posse.remove(livro)
           print(f"{livro.nome} devolvido com sucesso!")
       else:
           print(f"{livro.nome} não está em posse de {self.nome}")

    def status(self):
        return (f"Nome: {self.nome};\n"
                f"Contato: {self.contato};\n "
                f"Em posse: {[livro.nome for livro in self.em_posse]}\n")


ano = [livros.data for livros in livros]
anos = list(set(ano))
anos.sort()

contagem_por_anos = [ano.count(a) for a in anos]

plt.bar(anos, contagem_por_anos, color='blue')

plt.xlabel('Ano de publicação')
plt.ylabel('Número de livros')

plt.title("Distribuição de livros na Biblioteca")

for i, valor in enumerate(contagem_por_anos):
    plt.text(anos[i], valor, str(valor))

plt.show()