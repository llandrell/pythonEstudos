# =====================================================
# OPERADORES: in  e  not in
# =====================================================

# Strings são ITERÁVEIS
# Isso significa que podemos navegar caractere por caractere

# Os índices de uma string começam em 0
# e vão até o tamanho da string - 1

# Também é possível usar índices negativos:
# -1 representa o último caractere
# -2 o penúltimo, e assim por diante


# =====================================================
# EXEMPLOS COM ÍNDICES
# =====================================================

nome = 'André'

print(nome[0])
# 'A' → primeiro caractere (índice 0)

print(nome[2])
# 'd' → terceiro caractere (começa em zero)

print(nome[-1])
# 'é' → último caractere da string

# print(nome[-10])
# ERRO: índice fora do intervalo da string

print(nome[-5])
# 'A' → primeiro caractere usando índice negativo


# =====================================================
# OPERADOR in
# =====================================================

# O operador IN verifica se um valor EXISTE dentro de outro
# Retorna True se encontrar
# Retorna False se não encontrar

print('é' in nome)
# True → o Python percorre toda a string
# e verifica se o caractere 'é' está presente


# =====================================================
# OPERADOR not in
# =====================================================

# O operador NOT IN verifica se um valor NÃO EXISTE dentro de outro

print('lu' not in nome)
# True → a sequência 'lu' não existe na string "André"


# =====================================================
# MAIS EXEMPLOS PRÁTICOS
# =====================================================

print('A' in nome)
# True → diferencia maiúsculas de minúsculas

print('a' in nome)
# False → Python é case-sensitive

print('dr' in nome)
# True → verifica sequência de caracteres, não apenas letras isoladas

print('And' in nome)
# True

print('andre' in nome)
# False → letras minúsculas ≠ maiúsculas


# =====================================================
# EXEMPLO COM IF + in
# =====================================================

if 'é' in nome:
    print("O nome possui acento")
else:
    print("O nome não possui acento")


# =====================================================
# EXEMPLO REAL DO DIA A DIA
# =====================================================

email = 'andre@gmail.com'

if '@' in email and '.' in email:
    print("Email válido (verificação simples)")
else:
    print("Email inválido")