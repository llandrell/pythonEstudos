# =====================================================
# FORMATAÇÃO DE STRINGS COM f-strings (FORMA MODERNA)
# =====================================================

# Em f-strings, tudo dentro de {} é um PLACEHOLDER
# Após os dois pontos (:) definimos a FORMATAÇÃO

# Tipos de dados (histórico / referência):
# s → string
# d ou i → inteiro
# f → float (números com casas decimais)
# x ou X → hexadecimal

# Alinhamento e preenchimento:
# (caractere)(< > ^)(quantidade)
# < → alinhado à ESQUERDA
# > → alinhado à DIREITA
# ^ → centralizado

# Sinais:
# + → sempre mostra o sinal
# - → mostra apenas se for negativo

# = → força o sinal aparecer ANTES do preenchimento com zeros

# Flags de conversão:
# !r → chama __repr__()
# !s → chama __str__()
# !a → chama __ascii__()


# =====================================================
# EXEMPLOS PRÁTICOS
# =====================================================

variavel = 'ABCD'

print(f'{variavel}')
# ABCD

print(f'{variavel: >10}')
# Preenche com espaços à ESQUERDA até totalizar 10 caracteres

print(f'{variavel: <10}.')
# Preenche com espaços à DIREITA
# O ponto no final ajuda a visualizar os espaços

print(f'{variavel: ^10}')
# Centraliza o texto em 10 caracteres

print(f'{variavel:.^10}')
# Centraliza e usa '.' como caractere de preenchimento


# =====================================================
# FORMATAÇÃO DE NÚMEROS FLOAT
# =====================================================

print(f'{1000.484848:.2f}')
# Arredonda para 2 casas decimais


print(f'{1000.484848:0=+10,.2f}')
# Explicação detalhada:
# 0 → preenche com zero
# = → sinal vem antes do preenchimento
# + → sempre mostra o sinal
# 10 → largura total
# , → separador de milhar
# .2f → duas casas decimais

# Obs: é poderoso, mas raramente usado assim no dia a dia
# Normalmente usamos algo mais simples


# =====================================================
# HEXADECIMAL
# =====================================================

print(f'O hexadecimal de 1500 é {1500:08x}')
# 08 → preenche com zero até 8 caracteres
# x → hexadecimal em minúsculo


# =====================================================
# FLAGS DE CONVERSÃO
# =====================================================

print(f'{variavel!r}')
# Usa __repr__ → representação técnica (debug)

print(f'{variavel!s}')
# Usa __str__ → representação amigável (padrão)

print(f'{variavel!a}')
# Usa __ascii__ → caracteres não ASCII são escapados