'''
Docstring para 18.1-exercicio
fazer um programa que pergunte a hora ao usuário e, basenado-se no horario descrito, 
exija a saudação apropriada. ex
bom dia 0:00-11:59, boa tarde 12:00-17:59 e boa noite 18:00-23:59


'''

#forma melhorada


# Definição de uma função chamada "obter_saudacao"
# Função é um bloco de código reutilizável que executa uma tarefa específica.
def obter_saudacao(hora):

    # Verifica se a hora está entre 0 e 11 (inclusive)
    # 0 <= hora <= 11 é uma comparação encadeada
    # Significa: (hora >= 0) AND (hora <= 11)
    if 0 <= hora <= 11:
        return "Bom dia!"  # return devolve o valor e encerra a função

    # Se não for manhã, verifica se está entre 12 e 17
    elif 12 <= hora <= 17:
        return "Boa tarde!"

    # Se não entrou em nenhuma condição acima,
    # automaticamente será entre 18 e 23
    else:
        return "Boa noite!"


# while True cria um loop infinito
# True sempre é verdadeiro
# Então o bloco vai repetir para sempre
# Só para quando encontrar um "break"
while True:

    # input() pede algo ao usuário
    # O texto dentro dos parênteses é exibido na tela
    entrada = input("Digite um horário (HH:MM) ou 'sair' para encerrar: ")

    # .lower() transforma a string em minúscula
    # Isso permite aceitar "SAIR", "Sair", "sair", etc.
    if entrada.lower() == "sair":
        print("Programa encerrado.")

        # break interrompe o loop imediatamente
        # Sem ele, o while continuaria para sempre
        break

    # try significa: "tente executar isso"
    # Usamos quando existe risco de erro
    try:

        # split(":") divide a string onde houver ":"
        # Exemplo: "14:30" → ["14", "30"]
        hora_str, minuto_str = entrada.split(":")

        # Converte a parte da hora (texto) para número inteiro
        hora = int(hora_str)

        # Converte a parte do minuto (texto) para número inteiro
        minuto = int(minuto_str)

        # Verifica se os valores estão dentro de um horário válido
        # 0–23 para hora
        # 0–59 para minuto
        if 0 <= hora <= 23 and 0 <= minuto <= 59:

            # Chama a função obter_saudacao
            # Passa a hora como argumento
            # A função retorna uma string
            # print exibe essa string na tela
            print(obter_saudacao(hora))

        else:
            # Caso os números estejam fora do intervalo válido
            print("Horário inválido.")

    # except captura o erro caso aconteça
    # ValueError acontece se:
    # - não houver ":"
    # - o usuário digitar letras
    # - a conversão para int falhar
    except ValueError:
        print("Formato inválido. Use HH:MM.")
        












#forma bem simples de fazer

# horario = input("informe o horario que para receber uma saudação: (00:00) " )
# if (horario >= '00:00' and horario <= '11:59'):
#     print('Bom dia')
# elif (horario >= '12:00' and horario <= '17:59'):
#     print('Boa Tarde')
# elif (horario >= '18:00' and horario <= '23:59') :
#     print('Boa Noite')
# else:
#     print('digite um horario valido')