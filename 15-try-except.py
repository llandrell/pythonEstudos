# Introdução ao try/except
# try -> tenta executar um código que pode gerar erro
# except -> executado caso ocorra um erro esperado
# else -> executado somente se NÃO houver erro

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    # FAIL FAST:
    # Tentamos converter o valor o quanto antes.
    # Se não for um número, o erro acontece aqui.
    numero_float = float(numero_str)


#o valueError e o valor do erro que foi gerado, 
except ValueError:
    # Esse erro acontece quando o valor não pode ser convertido para float
    print('Erro: digite apenas números!')

else:
    # Só roda se não houve erro no try
    print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')