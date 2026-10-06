nome = "Ailton"
idade = 27
email = "ailton@email.com"
cidade = "Maringá"

# pessoa = {} # dict() -> também pode ser usado para criar um dicionário vazio

# também pode-se declarar da seguite forma:
# pessoa = dict(nome="Ailton",idade=25)
pessoa = {"nome": "Ailton", "idade": 25, "email": "ailton@email.com", "cidade": "Maringá"}

# ao acessar uma chave que não existe dá erro
# print(pessoa["documento"])

""" # pessoa.get("chave") -> acessar chave sem a possibilidade de erro
print(pessoa.get("documento")) # -> retorna None
# pessoa.get("chave", "alt") -> caso a chave não existir, retorna o alt
print(pessoa.get("chave", "N/A"))

# para alterar algum valor, pode ser feito por atribuição
pessoa["nome"] = "Léo"
# também pode ser atualizado com update({}), passando um dicionário com campos que já existam ou não
pessoa.update({"email": "leo@email.com", "company": "OneBitCode"})
print(pessoa)

# Meios de remover informação do dicionário
# remover usando del
# del pessoa["company"]
# remover usando pop() -> este retorna o elemento removido
pessoa.pop("idade")
print(pessoa) """

# =============================================================
# para acessar as chaves (keys) que tem no dicionário:
print(pessoa.keys())
# para acessar os valores (values) que tem no dicionário:
print(pessoa.values())
# para acessar as chaves+valores que tem no dicionário:
print(pessoa.items()) # -> retorna várias tuplas com chaves e valores

dados_lista = list(pessoa.items()) # -> transformando o resultado numa lista de tuplas
print(dados_lista[0][1]) # -> acessando a chave ou valor em uma posição específica

print("nome" in pessoa) # -> verificar se a chave "nome" existe no dicionário "pessoa"

usuario = {
    "nome": "João",
    "idade": 25,
    "endereço": {
        "rua": "Rua A",
        "numero": 123,
        "cidade": "São Paulo"
    }
} # -> exemplo de dicionário aninhado (um dicionário dentro de outro)

loja = {
    "nome": "Minha Loja",
    "produtos": [
        {"nome": "Notebook", "preco": 2500},
        {"nome": "Mouse", "preco": 50},
        {"nome": "Teclado", "preco": 120},
    ]
} # -> exemplo de dicionário com uma lista dentro, e esta lista contendo um dicionário

print(loja["produtos"]) # -> para acessar os valores da chave produtos (que é uma lista)
print(loja["produtos"][0]) # para acessar, dentro de produtos, um índice específico (já que é uma lista)
# para acessar, dentro de produtos, um índice específico e, neste índice, a chave nome
print(loja["produtos"][0]["nome"])