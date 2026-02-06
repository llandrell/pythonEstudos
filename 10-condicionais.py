# O controle de fluxo permite que o programa escolha caminhos diferentes.
# Pense nisso como uma bifurcação em uma estrada.

entrada = input("Você quer 'entrar' ou 'sair'? ").strip().lower() 
# .strip().lower() são boas práticas: removem espaços extras e deixam tudo em minúsculo.

# 1. O IF é sempre a primeira tentativa.
if entrada == 'entrar':
    # Este bloco só executa se a condição for True (Verdadeira)
    print('Você entrou no sistema.')
    print('Bem-vindo!')

# 2. O ELIF (else + if) só é testado se o IF lá de cima for False.
# Você pode ter quantos 'elifs' precisar entre o 'if' e o 'else'.
elif entrada == 'sair':
    print('Você saiu do sistema.')

# 3. O ELSE é o "porto seguro" ou "caso padrão". 
# Se NENHUMA das condições anteriores foi atendida, ele executa obrigatoriamente.
else:
    print('Opção inválida: você não digitou nem entrar nem sair.')

print("O programa continua aqui após a decisão.")   