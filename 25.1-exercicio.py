'''
faça uma lista de compras com LIST
o user deve ter a possibilidade de inserir, apagar e lista valores da sua lista
não permita que o programa quebre com erros de índices e enexistentes na lista.

'''
import os
lista_compra = []

while True:
    print('Lista de Compras')

    try: 
        
        number_digt = int(input(
        'Digite (1) para incerir um item.\n' \
        'digite 2 para listar\n' \
        'digite 3 para excluir\n' \
        'digite 4 para sair: '))
    except ValueError:
        print('Digite apenas números válidos.')
        continue

    match number_digt:
        
        case 1:
            lista_compra.append(input('Informe o item a ser inserido: '))
            print('Item adicionado com sucesso.')
            os.system('cls')
        case 2:
            os.system('cls')
            if not lista_compra:
                print('A lista está vazia.')
            else:
                for indice, item in enumerate(lista_compra):
                    print(indice, item)
            
        case 3:
            
            if not lista_compra:
                print('Lista vazia, nada para excluir.')
                continue

            try:
                indice = int(input('Informe o índice que deseja excluir: '))
                
                if 0 <= indice < len(lista_compra):
                    del lista_compra[indice]
                    print('Item removido com sucesso.')
                else:
                    print('Índice inválido.')
            
            except ValueError:
                print('Digite um número válido.')

        case 4:
            print('saindo do programa...')
            break 
        case _:
            os.system('cls')
            print('Digite um valor valido')


