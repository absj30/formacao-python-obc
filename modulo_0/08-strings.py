nome = "João_Silva"

# J o ã o _ S i l v a
# 0 1 2 3 4 5 6 7 8 9

print(nome[0]) # saída: "J"

"""
passar um index negativo faz com que seja lido de trás pra frente
Ex: nome = "João_Silva" --> se eu passar nome[-1] traz o último "a"
neste caso o primeiro índice de trás pra frente é [-1] e não zero
"""

print(nome[-1]) # saída: "a" 



# para pegar um pedaço da string coloca : no colchete do index
print(nome[0:3]) # saída: "Joã" - 0 inclusivo, 3 exclusivo
print(nome[0:4]) # saída: "João" - 0 inclusivo, 4 exclusivo
print(nome[:3]) # saída: "Joã" - desde o início [0], 3 exclusivo
print(nome[2:]) # saída: "ão Silva" - 2 inclusivo, até o final [9]
print(nome[:-2]) # saída: "João Sil" - desde o início [0], exceto os 2 últimos
print(nome[0:8:2]) # saída: "Jã_i" - 0 inclusivo, 8 exclusivo, pulando de 2 em 2
print(nome[::-1]) # saída: "avliS_oãoJ" - 0 e 9 OMITIDOS, pulando de trás pra frente de 1 em 1

# função len() - saber o tamanho da String
print(len(nome))

# f Strings -> para concatenar strings sem usar o + para concatenar

texto_sem_fstring = "Olá, seu nome é " + nome + "!"
print(texto_sem_fstring)
texto_com_fstring = f"Olá, seu nome é {nome}!"
print(texto_com_fstring)

# STRINGS SÃO IMUTÁVEIS
nome[0] = "W" # saída: TypeError: 'str' object does not support item assignment