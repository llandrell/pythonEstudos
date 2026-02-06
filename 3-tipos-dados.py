"""
TIPOS DE DADOS PRIMITIVOS EM PYTHON
===================================
Python: Linguagem de programação com tipagem DINÂMICA e FORTE
- Dinâmica: Não precisa declarar o tipo da variável
- Forte: Não converte tipos automaticamente
"""

# ========================================
# 1. STRINGS (str) - Textos entre aspas
# ========================================
print('String simples')           # Aspas simples
print("String com aspas duplas") # Aspas duplas
print("Aspas internas: 'OK'")    # Quando precisa de aspas dentro
print(r'Caminho: C:\users\doc')  # r = raw string (sem escape)
print('Escape manual: C:\\users') # \\ = uma barra invertida

# ========================================
# 2. NÚMEROS - int e float
# ========================================
print("\n=== NÚMEROS ===")
print(11)      # int positivo
print(-11)     # int negativo
print(1.1)     # float positivo
print(-1.1)    # float negativo

# Função TYPE() - mostra o tipo inferido
print(type(11))    # <class 'int'>
print(type(1.1))   # <class 'float'>

# ========================================
# 3. BOOLEANOS (bool) - True/False
# ========================================
print("\n=== BOOLEANOS ===")
print(10 == 10)    # True  (== COMPARA)
print(11 == 10)    # False
print('10' == 10)  # False (diferentes tipos!)

# Outros operadores que geram booleanos:
print(10 > 5)     # True
print(10 != 5)    # True (!= diferente)
print(10 >= 10)   # True

# ========================================
# 4. PRÁTICA - Exemplos do seu negócio
# ========================================
nome_cliente = "André"           # str
idade = 25                       # int
preco_reparo = 45.50             # float
tem_estoque = True               # bool

print(f"\n=== ORÇAMENTO WhatsApp ===")
print(f"Cliente: {nome_cliente}")
print(f"Idade: {idade} anos")
print(f"Reparo: R$ {preco_reparo}")
print(f"Estoque disponível: {tem_estoque}")

# ========================================
# 5. TUDO É OBJETO - Verificando tipos
# ========================================
print("\n=== TIPO DE CADA VARIÁVEL ===")
print(type(nome_cliente))  # <class 'str'>
print(type(idade))         # <class 'int'>
print(type(preco_reparo))  # <class 'float'>
print(type(tem_estoque))   # <class 'bool'>

print("\n✅ Saída completa executada!")