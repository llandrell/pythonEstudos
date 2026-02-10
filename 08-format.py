# a = 'A'
# b = 'B'
# c = 1.1

# # formato = 'a={1} b={0} c{2:.2f}'.format(a,b,c)


# parametros nomeados
formato = 'a={1} b={0} c{nome3:.2f}'.format(a,b,nome3=c)

print(formato)



# 1. TUDO no Python é OBJETO (tem tipo, memória, métodos)
a = 'A'        # str ← OBJETO com métodos como .upper(), .lower()
b = 'B'        # str ← OBJETO  
c = 1.1        # float ← OBJETO com métodos como .is_integer()

print(type(a))  # <class 'str'> ← PROVA que é objeto!
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>

# 2. OBJETOS têm MÉTODOS (funções "grudadas" no objeto)
print(a.upper())     # MÉTODO do objeto 'A' → 'A'
print(c.is_integer())# MÉTODO do objeto 1.1 → False

# 3. FUNÇÕES vs MÉTODOS
def funcao_global(x):    # FUNÇÃO (independente)
    return x * 2

obj = 'python'
print(funcao_global(obj))     # FUNÇÃO: recebe objeto como PARÂMETRO
print(obj.upper())           # MÉTODO: objeto chama a função nele mesmo

# 4. .format() - MELHORADO e CORRIGIDO
a = 'A'
b = 'B' 
c = 1.1

# ✅ CORRETO: Parâmetros por posição E nomeados
formato = '{1} vem antes de {0}, c={c:.2f}'.format(b, a, c=c)
print(formato)
# Saída: B vem antes de A, c=1.10

# 5. PARÂMETROS vs ARGUMENTOS
def exemplo(parametro1, parametro2):  # PARÂMETROS (placeholders)
    return parametro1 + parametro2

print(exemplo('A', 'B'))              # ARGUMENTOS (valores reais)
print(exemplo(parametro1='A', parametro2='B'))  # Argumentos NOMEAADOS