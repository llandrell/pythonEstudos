"""
Introdução ao empacotamento e desempacotamento em Python,
incluindo uso de listas e tuplas.

Empacotamento (packing) → Agrupar múltiplos valores em uma única variável.
Desempacotamento (unpacking) → Distribuir valores de uma estrutura
(iterável) em múltiplas variáveis.
"""

# ---------------------------
# EMPACOTAMENTO (Packing)
# ---------------------------

# Aqui estamos empacotando três valores dentro de uma lista.
# Lista é uma estrutura MUTÁVEL (podemos alterar seus valores).
nomes = ['Maria', 'Helena', 'Luiz']


# ---------------------------
# DESEMPACOTAMENTO (Unpacking)
# ---------------------------

# Desempacotamento clássico:
# nome1, nome2, nome3 = nomes
#
# Isso funciona porque a quantidade de variáveis
# precisa ser EXATAMENTE igual à quantidade de elementos.

# ---------------------------
# DESEMPACOTAMENTO COM "*"
# ---------------------------

# O operador "*" permite capturar múltiplos valores restantes.
# Ele sempre retorna uma LISTA com os valores capturados.

nome1, *resto = nomes

# Aqui acontece:
# nome1 recebe 'Maria'
# resto recebe ['Helena', 'Luiz']

# Importante:
# O "*" pode ser usado em qualquer posição:
# início, meio ou fim.


# ---------------------------
# BOAS PRÁTICAS
# ---------------------------

# Quando você NÃO vai usar uma variável,
# utilize "_" para indicar que ela será ignorada.
# Isso melhora a legibilidade do código.

# Exemplo 1: ignorando o primeiro valor
# _, nome2, *_ = nomes

# Exemplo 2: pegando primeiro e último elemento
# primeiro, *_, ultimo = nomes

# Observação importante:
# "_" é apenas uma convenção.
# Ele não tem comportamento especial na linguagem,
# mas é amplamente usado na comunidade Python.


# ---------------------------
# BOA PRÁTICA EXTRA
# ---------------------------

# Sempre garanta que a estrutura tenha elementos suficientes
# antes de desempacotar para evitar erro:
#
# ValueError: not enough values to unpack

if nomes:
    nome1, *resto = nomes
    print(nome1, resto)