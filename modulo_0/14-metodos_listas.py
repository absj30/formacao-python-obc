frutas = ["maçã", "banana", 123]
print(frutas)

# append - adiciona elemento ao final da lista
frutas.append("laranja")
print(frutas)

# insert - adiciona elemento no index especificado, "empurrando" os demais
# para os próximos índices
frutas.insert(2, "morango")
print(frutas)

# remove - remove o elemento da lista, passando o VALOR do item a ser removido
frutas.remove("laranja")
print(frutas)

# pop - remove o elemento da lista, passando o INDEX do item a ser removido
frutas.pop(3)
print(frutas)
# pop() sem parâmetro remove o último elemento
frutas.pop()
print(frutas)


# sort - ordena a lista em ordem crescente/alfabética
numeros = [4, 5, 2, 9, 7, 1]
numeros.sort()
print(numeros)
numeros.sort(reverse=True) # ordena de forma decrescente
print(numeros)

# index("el") - retorna o índex de "el" dentro da lista
print(frutas.index("banana"))

# join - transforma a lista em texto usando o separador -> exemplo: " e "
frutas_join = " e ".join(frutas)
print(frutas_join)

# split - transforma o texto em lista usando o separador -> exemplo: ", "
frutas_texto = "maçã, banana, abacaxi"
frutas_split = frutas_texto.split(", ")
print(frutas_split)

frutas_verdes = ["limão"]
frutas_vermelhas = ["maçã", "morango"]

novas_frutas = frutas_verdes + frutas_vermelhas
print(novas_frutas)