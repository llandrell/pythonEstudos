'''
Docstring para 19-while-brak

Rpetições em python, ja usei anteriormente...

While executa a ação enquanto uma condição ofr verdadeira.

'''

 


contador = 0  # Inicializa a variável contador com valor 0
contador_interno = 0 

while contador < 3 :   # enquanto a condição do while for veradeira vai execultar esse bloco de codigo
    # Enquanto contador for menor que 100,
    # o bloco abaixo continuará sendo executado.

    
    # Forma abreviada de: contador = contador + 1
    # Também existem: -=, *=, /=, //=, **=, %=

    # Se o contador for 6, não mostramos ele
    # if contador == 6:
    #     print('Não vou mostrar o 6')
    #     continue  
    #     # O continue faz o loop voltar para o início,
    #     # ignorando o restante do código abaixo.

    # # Se o contador estiver entre 10 e 26 (inclusive)
    # if 10 <= contador <= 26:
    #     print("Entrou no intervalo de 10 a 26")
    #     continue  
    #     # Volta para o início do while sem executar o que está abaixo
      # reiniando contador interno 
    while contador_interno < 5 :
        
        print(f'{contador= }, {contador_interno= }')
        contador_interno += 1
    contador_interno = 0  
        
    contador += 1  
    # Pergunta ao usuário se deseja sair do programa
    #nome = input('Deseja sair? Digite "sair" para encerrar: ')

   # if nome.lower() == 'sair':
      #  break  
        # O break encerra o loop imediatamente