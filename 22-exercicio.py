'''
Vamos pegar uma lista e mostrar os índices dessa lista.

'''

# Criamos uma variável chamada "lista"

# Estamos atribuindo a ela um objeto do tipo LIST
# Listas em Python são estruturas mutáveis e indexadas
lista = ['Maria', 'Helan', 'Luiz']

# O método append() adiciona um novo elemento
# sempre no FINAL da lista.
# Ele modifica a própria lista (não cria outra).
# Após essa linha, a lista terá 4 elementos.
lista.append('andre')

# Estrutura de repetição FOR
# range(len(lista)) funciona da seguinte forma:
#
# 1) len(lista) → retorna o tamanho da lista.
#    Agora temos 4 elementos.
#
# 2) range(4) → gera uma sequência numérica:
#    0, 1, 2, 3
#
# 3) A variável "i" receberá cada número dessa sequência
#    a cada repetição do laço.
#
# Ou seja, o laço executará 4 vezes.
for i in range(len(lista)):

    # print(i, lista[i]) faz duas coisas:
    #
    # 1) Mostra o valor de "i", que é o índice atual.
    #
    # 2) lista[i] acessa o elemento da lista
    #    usando indexação.
    #
    # Exemplo das iterações:
    # i = 0 → lista[0] = 'Maria'
    # i = 1 → lista[1] = 'Helan'
    # i = 2 → lista[2] = 'Luiz'
    # i = 3 → lista[3] = 'andre'
    #
    # Isso é chamado de iteração baseada em índice.
    print(i, lista[i])