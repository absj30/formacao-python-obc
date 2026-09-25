"""
Leia um nome completo e:
 Imprima em MAIÚSCULA
 Imprima em minúscula
 Contar quantas letras tem
 Extrair e imprimir as 3 primeiras letras
 Extrair e imprimir as 3 últimas letras
 Substituir espaços por underscore
"""
print("--- EXERCICIO 03 ---")
nome = input("Digite o nome completo: ")

print(f"""
MAIÚSCULA: {nome.upper()}
minúscula: {nome.lower()}
Quantidade de letras: {len(nome)}
Primeiras 3 letras: {nome[0:3]}")
Últimas 3 letras: {nome[-3:]}")
Com underscore: {nome.replace(" ", "_")}
""")