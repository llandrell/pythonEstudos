'''
Docstring para 19.-exercicio

Vamos itarar um string com while em python


'''


# Pede o nome do usuário.
# input() recebe o texto digitado.
# .split() divide a string em uma lista separando por espaços.
# "".join(...) junta novamente tudo sem espaço nenhum.
# Resultado: remove TODOS os espaços do nome.
nome = "".join(input("Digite seu nome: ").split())


# len(nome) retorna a quantidade de caracteres da string.
tamanho_nome = len(nome)


# Cria uma variável contador começando em 0.
# Ela será usada como índice para percorrer a string.
contador = 0


# Mostra o nome já sem espaços.
print(nome)


# Enquanto o contador for menor que o tamanho do nome:
# (evita erro de índice fora do limite)
while contador < tamanho_nome:
    
    # Acessa cada letra usando índice: nome[contador]
    # Adiciona um "*" após cada letra.
    # end='' impede que o print quebre linha.
    print(f'{nome[contador]}*', end='')
    
    # Incrementa o contador em 1 para ir para a próxima letra.
    contador += 1