produto1 = "Notebook"
produto2 = "Mouse"
produto3 = "Teclado"

lista = ["Notebook", "Mouse", "Teclado", 1, 2, 3.0, 4.0, True, None]

print(lista[0:3])
print(lista[-1])

print(lista[0])
lista[0] = "PC"
print(lista[0])

lista_numeros = list(range(0, 22, 3))
print(lista_numeros)
print(len(lista_numeros))