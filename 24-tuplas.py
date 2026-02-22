'''
Tuplas são parecidas com listas, porém são imutáveis.
Funcionam como uma constante para uma variável.
Sempre que você tiver um conjunto de valores que não precisam
ser alterados, é recomendado usar tuplas.
'''

# Criando uma tupla é simples: basta separar valores por vírgula.
# Os parênteses () são recomendados para deixar o código mais claro,
# mas tecnicamente não são obrigatórios.

# exemplo 1

#nomes = 'Matia', 'joão', 'elena'  # Isso já cria uma tupla automaticamente (empacotamento implícito)

nomes = ('Matia', 'joão', 'elena')  # criando uma tupla explicitamente com ()

# nomes[1] = 'joses'
# Isso geraria erro, pois tuplas não são mutáveis.
# TypeError: 'tuple' object does not support item assignment
# Funciona de forma parecida com string:
# não posso alterar o conteúdo sem criar um novo objeto.


# convertendo tupla em lista e lista em tupla

nomes = list(nomes)  # Convertendo para lista (agora é mutável)
print(type(nomes))

# Agora podemos alterar normalmente
nomes.append('moises')

# Após fazer as alterações necessárias,
# podemos converter novamente para tupla
nomes = tuple(nomes)  # Convertendo de volta para tupla (imutável)

# nomes.append('maria')
# Isso geraria erro novamente, pois tupla não possui método append()

print(type(nomes))

print(nomes[2])  
# Você consegue acessar (buscar) um item da tupla pelo índice,
# pois ela continua sendo indexada.
# O que não pode é modificar o valor.

# Sempre que precisar de uma lista, porém não precisar modificar
# seus valores depois da criação, use tupla.