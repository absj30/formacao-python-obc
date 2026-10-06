""" lista = ["Computador", "Mouse", "Monitor", "Cabo USB"]

# tuplas são listas imutáveis - declaradas com parênteses ()
tupla = ("Computador", "Mouse", "Monitor")

# tupla[0] = "Gabinete"
# -> saída: TypeError: 'tuple' object does not support item assignment

print(lista)
print(tupla)

# para declarar uma tupla de um só elemento, mesmo assim precisa por a vírgula
# no final
tupla2 = (42,)
print(type(tupla2))
# -> saída: <class 'tuple'>
"""

# sets são listas onde os elementos não se repetem
# sets não podem ser ordenados, eles se auto ordenam
# sets não podem ter um elemento acessado pelo índice (ex: numeros[0])
nomes = {"Arthur"}
# add -> adiciona um elemento
nomes.add("Ailton")
#print(nomes)

ferramentas = {"MARTELO", "SERROTE", "FURADEIRA", "CHAVE DE FENDA"}
#print(ferramentas)

# para adicionar vários elementos de uma vez
# observe que mesmo repetindo ele não adiciona de novo
ferramentas.update({"ALICATE", "SERROTE"})

# remove -> remove um elemento
# se o elemento não existir, lança um erro
ferramentas.remove("SERROTE")
#print(ferramentas)

# discard -> remove um elemento, mas se não existir, não lança erro
ferramentas.discard("BANANA")

# ===========================================================================
print("===========================================================================")
print("MÉTODOS PARA USAR ENTRE SETS")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# set1.union(set2) -> serve para unir 2 sets, respeitando a natureza de possuir apenas elementos únicos
# set1.intersection(set2) -> serve para verificar elementos comuns a ambos os sets
# set1.difference(set2) -> serve para ver o que tem no primeiro elemento mas não tem no segundo
resultado = set1.difference(set2)
print(resultado)

# Dados com duplicatas
emails = [
    "maria@example.com",
    "joao@example.com",
    "joao@example.com",  # Duplicado
    "pedro@example.com",
    "maria@example.com"  # Duplicado
]

# remove duplicatas
emails_unicos = set(emails)
print(emails_unicos)

# converter de volta para lista (se precisar ordenar)
emails_unicos_lista = list(emails_unicos)
emails_unicos_lista.sort()
print(emails_unicos_lista)