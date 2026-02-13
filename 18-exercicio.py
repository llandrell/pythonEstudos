"""
Exercício 18

Faça um programa que peça ao usuário para digitar um número.
- Se for inteiro → informar se é par ou ímpar.
- Se for float que representa inteiro (ex: 10.0) → tratar como inteiro.
- Caso não seja número → informar erro.
"""

# Função reutilizável
def eh_par(numero):
    return numero % 2 == 0


entrada = input("Digite um número: ")

try:
    numero = float(entrada)  # Tentamos converter para número
    #Converter para float para aceita 10.0 12.0 e etc

    # Verifica se o número é inteiro (mesmo sendo float)
    if numero.is_integer(): # numero.is_integer() É um método do tipo float. Ele verifica se o número
                            #decimal representa um inteiro.
        numero = int(numero)  # converte definitivamente para inteiro
        
        if eh_par(numero):
            print(f"O número {numero} é PAR.")
        else:
            print(f"O número {numero} é ÍMPAR.")
    else:
        print("Você digitou um número decimal que não é inteiro.")

except ValueError:
    print("Isso não é um número válido.")


# uma forma de verificar se é o numero inteiro
# if isinstance(number, int):
#     print("é um número inteiro")
#     number_int = number
# else:
#     print("Não é um número inteiro")

# segunda forma de verificar se o numero e inteiro
#.is_interger() É um método exclusivo de float
#precisa converter a string para float antes de verificar.
#Retorna True se o valor não tiver parte decimal
# if number.is_interger():
#     print("É um número inteiro (mesmo sendo float)")



# if number.isdigit():
#    # .isdigit() funciona apenas para inteiros positivos
#    # .isdigit() verifica se TODOS os caracteres da string são dígitos numéricos.

#    # Não aceita negativos (-10)

#    # Não aceita decimais (10.5)

#     print("É um número inteiro positivo")
# else:
#     print("Não é inteiro")
