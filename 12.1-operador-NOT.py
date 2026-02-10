# =====================================================
# OPERADOR LÓGICO "not"
# =====================================================

# O operador NOT é usado para INVERTER o valor lógico
# True  → False
# False → True

# Exemplos simples:
# not True  = False
# not False = True


# =====================================================
# EXEMPLO BÁSICO SEM NOT
# =====================================================

senha = input('Senha: ')

if senha == '123456':
    print('Senha correta')
else:
    print('Senha incorreta')


# =====================================================
# MESMO EXEMPLO USANDO NOT (forma equivalente)
# =====================================================

# O operador != significa "diferente de"
# Aqui estamos dizendo:
# "Se a senha NÃO for igual à senha permitida"

if senha != '123456':
    print('Senha incorreta')
else:
    print('Senha correta')


# =====================================================
# EXEMPLO PRÁTICO COM NOT + VALORES FALSY
# =====================================================

# Se o usuário não digitar nada, a variável 'senha'
# recebe uma string vazia '' (que é um valor FALSY)

if not senha:
    print("Você não digitou a senha")
else:
    print("Senha digitada")


# =====================================================
# NOT COM NÚMEROS E BOOLEANOS
# =====================================================

print(not 0)
# True → 0 é falsy, então not inverte para True

print(not 1)
# False → 1 é truthy

print(not False)
# True

print(not True)
# False


# =====================================================
# NOT EM EXPRESSÕES LÓGICAS
# =====================================================

idade = 16

# Sem NOT
if idade < 18:
    print("Menor de idade")

# Com NOT (inversão da condição)
if not idade >= 18:
    print("Menor de idade (usando not)")


# =====================================================
# NOT COM AND / OR (curto-circuito)
# =====================================================

usuario_logado = False
tem_permissao = False

# Se o usuário NÃO estiver logado
# OU NÃO tiver permissão, o acesso é negado
if not usuario_logado or not tem_permissao:
    print("Acesso negado")


# =====================================================
# RESUMO FINAL
# =====================================================

# not → inverte o valor lógico
# Muito usado para:
# - Verificar campos vazios
# - Negar condições
# - Deixar o código mais legível em alguns casos