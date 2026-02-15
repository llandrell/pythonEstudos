# Criando uma calculadora em Python
# O programa pede dois números e um operador matemático

# while True cria um loop infinito
# O código dentro dele vai repetir até encontrar um break

def sair_programa():  # Define uma função para perguntar se o usuário quer sair
    sair = input('Deseja sair? [s]im, [n]ão: ').lower().startswith('s')# .input('') Pergunta ao usuário, .lower() Converte a resposta para minúsculo .stratswuth('s') Verifica se começa com a letra "s"

    return sair  # Retorna True se começar com "s", caso contrário False


while True:  # Início do loop principal (repete até dar break)

    try:  # Tenta executar o bloco abaixo

        # input() recebe texto do usuário
        # .strip() remove espaços no começo e no fim
        # int() converte o texto para número inteiro
        # Se o usuário digitar algo inválido (ex: letra),
        # o int() gera um ValueError

        numero1 = int(input('Informe o primeiro número: ').strip())  # Pede o primeiro número
        numero2 = int(input('Informe o segundo número: ').strip())   # Pede o segundo número

    except ValueError:  # Se ocorrer erro de conversão para inteiro
        print("Erro: Você deve digitar apenas números inteiros.")  # Mostra mensagem de erro
        
        if sair_programa():  # Pergunta se deseja sair
            break  # Encerra o loop
        
        continue  # Volta para o início do loop

    else:  # Executa apenas se NÃO houve erro no try

        # Recebe o operador matemático
        # .strip() remove espaços extras
        operador = input('Informe a operação (+, -, *, /): ').strip()

        # Verifica se o operador digitado é válido
        if operador not in ['+', '-', '*', '/']:
            print("Erro: Operador inválido.")  # Mensagem de erro
            
            if sair_programa():  # Pergunta se deseja sair
                break  # Encerra o loop
            
            continue  # Volta para o início do loop

        else:  # Se o operador for válido

            if operador == '+':  # Se for soma
                print(f'o Resultado da Soma de {numero1=} + {numero2=} e = {numero1+numero2}')

            elif operador == '-':  # Se for subtração
                print(f'o Resultado da Subtração de {numero1=} - {numero2=} e = {numero1-numero2}')

            elif operador == '*':  # Se for multiplicação
                print(f'o Resultado da Multiplicação de {numero1=} * {numero2=} e = {numero1*numero2}')

            elif operador == '/':  # Se for divisão
                # Atenção: se numero2 for 0 aqui dará erro ZeroDivisionError
                print(f'o Resultado da Divisão de {numero1=} / {numero2=} e = {numero1/numero2}')
            else:
                print('não deveria chegar aqui! NUNCA!')


    # ----------------------------
    # Segunda versão (usando dicionário)
    # ----------------------------

    try:  # Novo bloco try para a segunda versão

        # Novamente pede dois números ao usuário
        numero1 = int(input('Informe o primeiro número: ').strip())
        numero2 = int(input('Informe o segundo número: ').strip())

    except ValueError:  # Caso o usuário digite algo inválido
        print("Erro: Digite apenas números inteiros.")
        
        if sair_programa():  # Pergunta se deseja sair
            break  # Encerra o loop
        
        continue  # Reinicia o loop

    else:  # Se não houver erro

        operador = input('Informe a operação (+, -, *, /): ').strip()  # Pede o operador

        # Cria um dicionário chamado "operacoes"
        # Cada chave representa um operador
        # Cada valor é o resultado correspondente

        operacoes = {
            '+': numero1 + numero2,  # Soma
            '-': numero1 - numero2,  # Subtração
            '*': numero1 * numero2,  # Multiplicação

            # Operador ternário:
            # Se numero2 for diferente de 0 → faz a divisão
            # Caso contrário → retorna mensagem de erro
            '/': numero1 / numero2 if numero2 != 0 else "Erro: divisão por zero"
        }

        # Verifica se o operador existe no dicionário
        if operador in operacoes:
            print(f"Resultado: {operacoes[operador]}")  # Mostra o resultado
        else:
            print("Erro: Operador inválido.")  # Caso operador não exista
            
            if sair_programa():  # Pergunta se deseja sair
                break  # Encerra o loop
            
            continue  # Volta ao início do loop