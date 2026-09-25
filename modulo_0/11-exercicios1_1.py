"""
Leia um número inteiro e imprima:
 O número
 Seu antecessor (n - 1)
 Seu sucessor (n + 1)
"""
print("--- EXERCICIO 01 ---")
numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"""
Numero: {numero}
Antecessor: {antecessor}
Sucessor: {sucessor}
""")