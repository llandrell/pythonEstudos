# ==============================
# Comentários em Python
# ==============================

# Comentários são trechos de texto que explicam o código,
# mas NÃO são executados pelo interpretador.
# Tudo o que vem depois do símbolo "#" é ignorado pelo Python.

# Exemplo de comando para imprimir algo na tela:
print('Hello, world!')  # Exibe a mensagem 'Hello, world!' no console

# Podemos imprimir outras mensagens também:
print('Comentários não são interpretados pelo código.')

# ----------------------------------------
# Docstrings: textos entre aspas triplas
# ----------------------------------------
"""
Docstrings (documentação de strings) não são comentários de verdade,
mas servem para documentar blocos de código, funções, classes ou módulos.

Diferente do comentário simples (#),
o interpretador do Python lê a docstring e a armazena internamente.
Ela pode ser acessada pelo comando help() ou pelo atributo __doc__.
"""

'''
Também é possível usar aspas simples triplas para criar uma docstring.
O resultado é o mesmo, apenas muda o tipo de aspas.
'''

# Exemplo ilustrando que docstrings podem ser usadas em funções:
def saudacao():
    """
    Esta função imprime uma saudação simples na tela.
    """
    print("Olá! Seja bem-vindo ao Python!")

# Chamando a função
saudacao()