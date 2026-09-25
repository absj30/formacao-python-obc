# string.metodo()

texto = "Python"
texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()

print(texto_maiusculo)
print(texto_minusculo)

# string.strip() -> remove todos espaços em branco do início e do final
# string.rstrip() -> remove todos espaços em branco do final (à direita)
# string.lstrip() -> remove todos espaços em branco do início (à esquerdaa)
email = "   ailton@onebitcode.com              "
print("Sem strip: ",len(email))
print("Com strip: ", len(email.strip()))

print(email.strip().endswith(".com"),"\n")


# string.replace("aaa", "bbb", X) -> substitui o texto "aaa" por "bbb" nas X primeiras ocorrências
# se não informar o X ele substitui em todas as ocorrências
texto2 = "Olá, mundo! Tudo bem, mundo? O mundo"
novo_texto2 = texto2.replace("mundo", "Python", 2)
print(texto2)
print(novo_texto2)

# string.find("a", X, Y) -> retorna a primeira ocorrência, entre os índices X a Y
# se não informar X e Y retorna a primeira ocorrência de "a" da string toda
print(texto2.find("mundo?"))

# string.count("abc") -> retorna a quantidade de ocorrências de "abc" na string
print(texto2.count("mundo!"))

# FUNÇÕES DE VALIDAÇÃO

print("123".isdigit())      # True (só números)
print("abc".isdigit())      # False

print("abc".isalpha())      # True (só letras)
print("abc123".isalpha())   # False

print("abc123".isalnum())   # True (letras e números)
print("abc 123".isalnum())  # False (tem espaço)