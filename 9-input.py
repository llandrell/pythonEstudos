# Em sistemas reais, os dados viriam de um request (JSON), formulário ou Banco de Dados.
# O input é excelente para automações (scripts CLI) e testes rápidos.

entrada_1 = input("Digite um número: ")
entrada_2 = input("Digite outro número: ")

# Por que não converter no input? 
# Porque se o usuário digitar "A", o programa para aqui com um ValueError.
# O ideal é capturar como string e validar depois.



''' O 'try' (tentar) marca o início de um bloco de código que pode ser perigoso.
"Perigoso" significa que algo ali dentro pode gerar um erro que o Python não sabe resolver sozinho.
'''
try:
    # O Python vai tentar executar estas linhas em ordem:
    # Convertendo os dados após a captura (Checagem)
    numero_1 = int(entrada_1)# Se o usuário digitou 'A', o erro nasce EXATAMENTE aqui.
    numero_2 = int(entrada_2)

    # Se ocorrer um erro em qualquer linha acima, o Python PARA imediatamente 
    # de executar o bloco 'try' e pula direto para o 'except'.
    soma = numero_1 + numero_2

    # Usando o f-string com '=' para debug (mostra nome_da_var=valor)
    print(f"DEBUG: {numero_1=}, {numero_2=}")
    
    print(f"A soma dos números digitados é: {soma}")


# O 'except' (exceção/erro) é o plano de contingência. 
# Ele só é executado SE o código dentro do 'try' falhar.
# 'ValueError' é o nome do erro específico para quando tentamos converter letras em números.
except ValueError:
    # Em vez de o programa fechar com uma mensagem técnica feia, 
    # ele executa o que você programar aqui:
    print("Erro: Você não digitou números inteiros válidos.")

# O programa continua vivo daqui para baixo, independentemente do erro!
print("Fim do processamento.")