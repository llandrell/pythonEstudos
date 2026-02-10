# =====================================================
# OPERADORES LÓGICOS EM PYTHON
# and (e), or (ou) e not (negação)
# =====================================================

# -------------------------------
# AND:
# Retorna True somente se TODAS as condições forem verdadeiras.
# Se QUALQUER condição for falsa, toda a expressão será False.
# -------------------------------

# Em Python, alguns valores são considerados FALSY (avaliados como False):
# 0, 0.0, '', False e None
#
# Todo outro valor é considerado TRUTHY (avaliado como True)

# None representa a ausência de valor
# (não é zero, nem string vazia)


# =====================================================
# EXEMPLO DE ENTRADA DO USUÁRIO
# =====================================================

# entrada = input('[E] Entrar | [S] Sair: ').upper()
# senha_permitida = '123456'


# =====================================================
# PRIMEIRA ESTRUTURA CONDICIONAL
# =====================================================

# if entrada == 'E':
#     print("Entrou")
# elif entrada == 'S':
#     print("Saiu")
# else:
#     print("Opção inválida")


# =====================================================
# VALIDAÇÃO COM SENHA (VERSÃO SIMPLES)
# =====================================================

# senha_digitada = input("Digite a senha: ")

# if entrada == 'S':
#     print("Saiu")
# elif entrada == 'E' and senha_digitada == senha_permitida:
#     print("Entrou")
# else:
#     print("Acesso negado")


# =====================================================
# VALIDAÇÃO COM SENHA (VERSÃO MAIS ORGANIZADA)
# =====================================================

# Essa versão é melhor porque:
# - Só pede a senha quando realmente precisa
# - Evita verificações desnecessárias
# - Facilita a leitura e manutenção do código

# if entrada == 'S':
#     print("Saiu")
# elif entrada == 'E':
#     senha_digitada = input("Digite a senha: ")
#     if senha_digitada == senha_permitida:
#         print("Entrou")
#     else:
#         print("Senha incorreta")
# else:
#     print("Opção inválida")


# =====================================================
# TESTES COM OPERADOR AND
# =====================================================

# print(True and True)
# True → todas as condições são verdadeiras

# print(True and True and False)
# False → existe pelo menos uma condição falsa

# print(True and bool(0))
# False → 0 é um valor falsy

# print(True and bool(0.0))
# False → 0.0 também é um valor falsy


# =====================================================
# CURTO-CIRCUITO (SHORT-CIRCUIT) COM AND
# =====================================================

# O Python avalia expressões da esquerda para a direita.
# No operador AND, ao encontrar o primeiro False,
# a avaliação é interrompida (curto-circuito).

# print(True and False and not True)
# False → o "not True" nem chega a ser avaliado


# =====================================================
# OPERADOR OR
# =====================================================

# OR:
# Se QUALQUER condição for verdadeira,
# toda a expressão será avaliada como True.


# =====================================================
# EXEMPLO PRÁTICO COM OR (DIDÁTICO + CLEAN CODE)
# =====================================================

entrada = input('[E] Entrar | [S] Sair: ')
senha_permitida = '123456'

# -----------------------------------------------------
# EXEMPLO DIDÁTICO DO USO DO OR
# Aqui mantemos comparações repetidas propositalmente
# para demonstrar como o operador OR funciona.
# -----------------------------------------------------

if entrada == 'S' or entrada == 's':
    print("Saiu")

elif entrada == 'E' or entrada == 'e':

    # Curto-circuito com OR:
    # Se o usuário apenas pressionar ENTER,
    # input() retorna '' (string vazia).
    # '' é FALSY, então 'sem senha' será usado.
    senha_digitada = input("Digite a senha: ") or 'sem senha'

    if senha_digitada == senha_permitida:
        print("Entrou")
    else:
        print("Senha incorreta")

else:
    print("Opção inválida")


# -----------------------------------------------------
# FORMA RECOMENDADA (BOA PRÁTICA / CLEAN CODE)
# -----------------------------------------------------

# Normalizamos a entrada para evitar comparações repetidas
entrada = entrada.upper()

if entrada == 'S':
    print("Saiu (forma recomendada)")

elif entrada == 'E':
    senha_digitada = input("Digite a senha: ") or 'sem senha'
    if senha_digitada == senha_permitida:
        print("Entrou (forma recomendada)")
    else:
        print("Senha incorreta (forma recomendada)")

else:
    print("Opção inválida (forma recomendada)")