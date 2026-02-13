'''

Exercício 18.2

Peça o primeiro nome do usuário.
- Se tiver 4 letras ou menos → "Seu nome é curto"
- Se tiver entre 5 e 6 letras → "Seu nome é normal"
- Se tiver mais que 6 letras → "Seu nome é muito grande"

'''


#metodo simples 
# nome = input("Escreva seu nome: ")

# if len(nome) <= 4:
#     print("Seu nomé e curto")
# elif 5 <= len(nome) <= 6 :
#     print("Seu nomé é Normal")
# else:
#     print("Seu nomé é Muito Grande")


#metodo mais proficional

# input() recebe texto do usuário
# .strip() remove espaços antes e depos
nome = input("Escreva seu primeiro nome: ").strip()

# len() é uma função embutida do Python
# Ela retorna a quantidade de caracteres da string
tamanho = len(nome)

# Verifica se o nome está vazio
if tamanho == 0:
    print("Você não digitou nenhum nome.")

# Se tiver 4 letras ou menos
elif tamanho <= 4:
    print("Seu nome é curto.")

# Se tiver entre 5 e 6 letras
elif 5 <= tamanho <= 6:
    print("Seu nome é normal.")

# Se for maior que 6
else:
    print("Seu nome é muito grande.")



