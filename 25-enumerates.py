'''
enumerate - enumera iteráveis, ou seja, adiciona um índice automático
a cada elemento do iterável (lista, tupla, string, etc).
'''

# Ou seja, o último exercício feito com range(len(lista))
# ficaria bem mais simples usando enumerate.


# exemplos:
'''
Vamos pegar uma lista e mostrar os índices dessa lista.
'''

# Criamos uma variável chamada "lista"
# Estamos atribuindo a ela um objeto do tipo LIST.
# Listas em Python são estruturas:
# - Mutáveis (podem ser alteradas)
# - Ordenadas
# - Indexadas (começam do índice 0)
lista = ['Maria', 'Helan', 'Luiz']

# O método append() adiciona um novo elemento
# sempre no FINAL da lista.
# Ele modifica a própria lista (não cria outra).
# Após essa linha, a lista terá 4 elementos.
lista.append('andre')


# -------------------------------
# FORMA ANTIGA (usando range)
# -------------------------------

# Estrutura de repetição FOR
# range(len(lista)) funciona da seguinte forma:
#
# 1) len(lista) → retorna o tamanho da lista.
#    Agora temos 4 elementos.
#
# 2) range(4) → gera uma sequência numérica:
#    0, 1, 2, 3
#
# 3) A variável "i" recebe cada número dessa sequência
#    a cada repetição do laço.
#
# Isso é chamado de iteração baseada em índice.
#
# for i in range(len(lista)):
#     print(i, lista[i])


# -------------------------------
# USANDO ENUMERATE (FORMA MODERNA)
# -------------------------------

# enumerate(lista) retorna um objeto iterador.
# Ele produz pares no formato: (indice, valor)

lista_enumerada = enumerate(lista)

# Como enumerate retorna um ITERADOR,
# podemos usar next() para pegar os valores manualmente.

print(next(lista_enumerada))  # (0, 'Maria')
print(next(lista_enumerada))  # (1, 'Helan')
print(next(lista_enumerada))  # (2, 'Luiz')
print(next(lista_enumerada))  # (3, 'andre')

# Agora o iterador foi totalmente consumido.
# Se tentarmos continuar, ele não terá mais valores.

for item in lista_enumerada:
    print(item)  # não imprime nada, pois já foi consumido

# Convertendo para lista após consumir o iterador
# também resultará em lista vazia.
print(list(lista_enumerada))  # []


# -------------------------------
# FORMA MAIS UTILIZADA NA PRÁTICA
# -------------------------------

# O mais comum é usar enumerate diretamente no for.
# Assim, a cada loop ele cria um novo iterador.

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    print(item)

# Forma mais legível e profissional:
# Desempacotando diretamente índice e valor.

for indice, nome in enumerate(lista):
    print(indice, nome)


# -------------------------------
# MELHORANDO A LEGIBILIDADE
# -------------------------------

# Se você apenas imprimir enumerate(lista),
# verá algo como:
# <enumerate object at 0x00000...>
# que não é muito legível.

# Para visualizar melhor, convertemos em lista ou tupla:
listas = list(enumerate(lista))

print(listas)