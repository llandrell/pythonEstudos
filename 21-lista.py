'''
Uma lista em Python é uma estrutura de dados usada para armazenar vários valores dentro de uma única variável.

Ela pode ser comparada a:
    - Uma matriz na matemática (em conceito de organização)
    - Um array no JavaScript
Ou seja, é uma coleção de elementos organizados em sequência.

Características principais:

    - Ordenada → mantém a ordem em que os elementos foram inseridos
    - Mutável → pode ser alterada depois de criada
    - Permite valores repetidos
    - Pode armazenar tipos diferentes
    - Suporta vários valores de qualquer tipo na mesma estrutura

Métodos úteis:

    append() → adiciona um elemento ao final da lista
    insert() → adiciona um elemento em posição específica
    remove() → remove pelo valor → frutas.remove("uva")
    pop() → remove pelo índice → frutas.pop(0)
    del → remove pelo índice ou pode apagar a lista inteira
    clear() → remove todos os elementos da lista, mas mantém a lista existente
    extend() → adiciona vários elementos de outra lista dentro da lista atual

Boa prática:
    Em listas muito grandes, é recomendado trabalhar principalmente
    no início ou no final (como pilha ou fila),
    pois inserir ou remover no meio da lista exige
    movimentação dos elementos na memória,
    gerando maior custo de processamento.
'''

# lista = []  # Criando uma lista vazia
# Lista é um tipo mutável (principal diferença em relação à string, que é imutável)

lista = [123, True, 'Luiz', 1.2, []]  
# Uma lista suporta diferentes tipos de dados,
# inclusive outra lista dentro dela

lista[2] = 'Maria'  
# Alterando o valor do índice 2
print(lista)

del lista[0]  
# Deletando o elemento do índice 0
print(lista)

lista.append(50)  
# Adicionando valor ao final da lista
print(lista)

valor_removido = lista.pop()  
# Remove o último elemento
# pop() também retorna o valor removido
print(lista, valor_removido)

lista.pop(2)  
# Removendo elemento pelo índice
print(lista)

lista.append(1234)
print(lista)

del lista[-1]  
# Remove o último elemento usando índice negativo
print(lista)

lista.insert(0, 'André')  
# Insere um elemento no índice 0
# Primeiro argumento é o índice, segundo é o valor

lista_a = [1, 2, 3]
lista_b = ['andre', 'rafael', 'thiago']

lista_c = lista_a + lista_b  
# Concatenando duas listas e criando uma nova lista
print(lista_a, lista_b, lista_c)

lista_c.append('nova edição')
print(lista_a, lista_b, lista_c)  
# Modificar lista_c não altera lista_a nem lista_b

lista_a.extend(lista_b)  
# Aqui estamos modificando lista_a
# Adicionando todos os elementos de lista_b nela
print(lista_a)

lista_a.pop()
print(lista_a, lista_b)  
# Remove apenas da lista_a
# Não existe vínculo entre lista_a e lista_b


'''
Cuidados importantes com dados mutáveis em Python:

Em Python, variáveis não guardam diretamente os valores.
Elas guardam referências (endereços de memória) para os objetos.

Para tipos imutáveis (int, str, tuple):
    = cria um novo valor quando modificado.

Para tipos mutáveis (list, dict, set):
    = faz a variável apontar para o mesmo objeto na memória.

Ou seja, duas variáveis podem apontar para a mesma lista.
Se uma modificar, a outra também "enxerga" a modificação.
'''

# Criando a primeira lista
lista_1 = ['Luiz', 'Maria']

# Aqui NÃO é criada uma nova lista.
# lista_2 passa a apontar para o MESMO objeto na memória.
lista_2 = lista_1

# Modificando o índice 0
# Estamos alterando o objeto original
lista_1[0] = 'Qualquer valor'

# Como lista_2 aponta para o mesmo objeto,
# ela também reflete a alteração
print(lista_2)  # ['Qualquer valor', 'Maria']

# Agora modificamos usando lista_2
lista_2[0] = 'Outro valor'

# Como ambas apontam para o mesmo objeto,
# lista_1 também é afetada
print(lista_1)  # ['Outro valor', 'Maria']




#diferenças:
'''concatenação de lista'''
#lista1 = [1, 2]
#lista2 = [3, 4]

#lista3 = lista1 + lista2
#print(lista3)

#aqui É criada uma nova lista
#Os elementos de lista1 e lista2 são copiados
#lista1 e lista2 permanecem intactas
#não altera as listas originais, ele cria outra lista.

'''append() de lista'''

#lista1 = [1, 2]
#lista2 = [3, 4]

#lista1.append(lista2)
#print(lista1)

#append() adiciona um único elemento
#Esse elemento é a lista inteira lista2
#Perceba que virou uma lista dentro de outra lista (lista aninhada).


''' apontando para o mesmo endereço na memoria'''
#lista1 = [1, 2]
#lista2 = [3, 4]

#lista1 = lista2
#Não há cópia
#lista1 passa a apontar para o mesmo objeto que lista2
#lista1 ──► [3, 4] ◄── lista2
#Se modificar uma: tambem modifica a outra

#lista1 = [1, 2]
#lista2 = [3, 4]

#lista1.extend(lista2)
#print(lista1)

#extend() pega cada elemento de lista2
#Adiciona um por um no final de lista1
#Modifica lista1
#Não cria nova lista
#lista2 continua intacta

'''
append() → coloca uma caixa dentro da outra 

extend() → despeja o conteúdo da caixa 

+ → cria uma caixa nova com tudo junto 

= → faz duas variáveis apontarem para a mesma caixa 
'''
