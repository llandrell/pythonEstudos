"""
4-conversao-tipos

A conversão de tipos (também conhecida como type conversion, typecasting ou coerção)
é o processo de converter um valor de um tipo de dado para outro. Em Python, isso é
essencial para operações entre tipos incompatíveis, como somar números e strings.

Tipos primitivos e imutáveis principais:
- str (string): texto, ex: '123'
- int (inteiro): números inteiros, ex: 123
- float (ponto flutuante): números decimais, ex: 123.45
- bool (booleano): True ou False

Conversões explícitas usam funções como int(), str(), float() e bool().
Python não faz coerção implícita ampla (ex: int + str gera erro).
Sempre verifique tipos com type() ou isinstance() antes de operar.
"""
print(1 + 1)  # 2 (soma de inteiros)
# print('um' + 1)  # TypeError: não pode concatenar str com int
print('um' + 'dois')  # 'umdois' (concatenação de strings)
print('1', type('1'))  # '1' <class 'str'> (string, não número)
a = int('1')  # Conversão explícita: str -> int
print(a, type(a))  # 1 <class 'int'> (agora é inteiro)

# Exemplos adicionais úteis:
print(str(123) + ' itens')  # '123 itens' (int -> str para concatenar)
print(float('3.14'))  # 3.14 (str -> float)
print(int(3.99))  # 3 (float -> int, arredonda para baixo)
print(bool(0))  # False (int -> bool, 0 é falso)
print(bool(42))  # True (qualquer não-zero é True)