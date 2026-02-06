"""
6-operadores-aritmeticos-python

Operadores aritméticos em Python
--------------------------------
- Adição:            a + b
- Subtração:         a - b
- Multiplicação:     a * b
- Divisão real:      a / b         (resultado float)
- Divisão inteira:   a // b        (descarta as casas decimais)
- Exponenciação:     a ** b        (a elevado a b; cuidado com números muito grandes)
- Módulo:            a % b         (resto da divisão inteira)

Boas práticas (estilo código limpo):
- Use nomes de variáveis descritivos em vez de letras soltas, como soma, diferenca, produto.
- Evite comentários óbvios; deixe o código se explicar o máximo possível.
- Agrupe exemplos relacionados e use espaçamento consistente ao redor de operadores.
- Mostre exemplos reais e legíveis, facilitando manutenção e estudo.
"""

# Exemplos básicos de operadores aritméticos
soma = 10 + 10
print("Soma:", soma)

subtracao = 10 - 5
print("subtração:", subtracao)

multiplicacao = 10 * 10
print("Multiplicação:", multiplicacao)

divisao_real = 10 / 2.2
print("Divisão real:", divisao_real)

divisao_inteira = 10 // 2
print("Divisão inteira:", divisao_inteira)

exponenciacao = 6 ** 3
print("Exponenciação (6 ** 3):", exponenciacao)

resto_modulo = 29 % 5
print("Resto (29 % 5):", resto_modulo)

# Operadores com strings (repetição e concatenação)
nome = "Luiz"
print("Repetição de caractere:", "A" * 3)      # 'AAA'
print("Repetição de string:", 3 * nome)        # 'LuizLuizLuiz'

parte_nome = "An"
segunda_parte_nome = "dre"
nome_completo = parte_nome + segunda_parte_nome
print("Concatenação:", nome_completo)

# Precedência dos operadores aritméticos
"""
Ordem de precedência (do mais forte para o mais fraco):
1 - (expressões) entre parênteses
2 - **  exponenciação
3 - *  /  //  % (multiplicação, divisão, divisão inteira e modulo)
4 - +  - (soma e subtração)

Exemplo: 2 + 3 * 4 ** 2
1) 4 ** 2  -> 16
2) 3 * 16  -> 48
3) 2 + 48  -> 50
"""

expressao = 2 + 3 * 4 ** 2
print("Resultado da expressão 2 + 3 * 4 ** 2:", expressao)