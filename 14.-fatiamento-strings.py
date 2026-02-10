# =====================================================
# FATIAMENTO DE STRINGS EM PYTHON
# =====================================================

# Fatiamento usa a sintaxe:
# [inicio : fim : passo]

# inicio → índice inicial (inclusivo)
# fim → índice final (exclusivo)
# passo → intervalo entre os caracteres

# OBS:
# - Índice começa em 0
# - Índices negativos começam do final
# - A função len() retorna a quantidade de caracteres da string


variavel = "Ola Mundo"


# =====================================================
# ACESSO DIRETO POR ÍNDICE
# =====================================================

print(variavel[-4])
# 'u' → quarto caractere a partir do final


# =====================================================
# TAMANHO DA STRING
# =====================================================

print(len(variavel))
# 9 → quantidade total de caracteres (contagem, não índice)


# =====================================================
# FATIAMENTOS SIMPLES
# =====================================================

print(variavel[4:])
# 'Mundo' → do índice 4 até o final

print(variavel[4:9])
# 'Mundo' → do índice 4 até o 8 (9 não entra)

print(variavel[:4])
# 'Ola ' → do início até o índice 3

print(variavel[3:-3])
# ' Mu' → começa no índice 3 e vai até 3 antes do final


# =====================================================
# ÍNDICE x CONTAGEM
# =====================================================

# Índice é a posição (começa em 0)
# Contagem é a quantidade (começa em 1)

# Por isso:
# len(variavel) == 9
# último índice == 8


# =====================================================
# FATIAMENTO COM PASSO
# =====================================================

print(variavel[0:9:1])
# 'Ola Mundo' → passo 1 (padrão)

print(variavel[0:9:3])
# 'O M' → pega de 3 em 3 caracteres


# =====================================================
# INVERTENDO STRING (MUITO USADO)
# =====================================================

print(variavel[::-1])
# 'odnuM alO' → string invertida


print(variavel[-1:-10:-1])
# 'odnuM alO' → mesma coisa, forma explícita