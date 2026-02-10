'''
Operadores de compração (relacionias)


Operadores de comparação (relacionais)

| Operador | Significado           | Exemplo   | Resultado |
|----------|-----------------------|-----------|-----------|
| >        | Maior que             | 2 > 1     | True      |
| >=       | Maior ou igual        | 2 >= 2    | True      |
| <        | Menor que             | 1 < 2     | True      |
| <=       | Menor ou igual        | 2 <= 2    | True      |
| ==       | Igual a               | 'a' == 'a'| True      |
| !=       | Diferente de          | 'a' != 'b'| True      |


'''
# Exemplos de operadores de comparação retornando True ou False

maior = 2 > 1          # True  -> 2 é maior que 1
maior_igual = 2 >= 3   # False -> 2 NÃO é maior ou igual a 3
menor = 1 < 2          # True  -> 1 é menor que 2
menor_igual = 2 <= 3   # True  -> 2 é menor ou igual a 3
igual = 'a' == 'a'     # True  -> as duas strings são iguais
diferente = 'a' != 'b' # True  -> as strings são diferentes

# Exibe o nome da variável e o valor (recurso do f-string: expressão seguida de =)

print(f'{maior=} {maior_igual=} {menor=} {menor_igual=} {igual=} {diferente=}')


'''
maior = 2 > 1: compara 2 e 1; como 2 é maior, o resultado é True, que é armazenado em maior.

maior_igual = 2 >= 3: verifica se 2 é maior ou igual a 3; como não é, o resultado é False.

menor = 1 < 2: 1 é menor que 2, então True.

menor_igual = 2 <= 3: 2 é menor ou igual a 3, então True.

igual = 'a' == 'a': compara duas strings; como são iguais, True.

diferente = 'a' != "b": compara 'a' e "b"; como são diferentes, True.

No print(...), o formato variavel= dentro da f-string mostra nome e valor de cada variável, por exemplo: maior=True.

'''