"""
Exercício 20.2
Criar um jogo onde o usuário precisa adivinhar uma palavra secreta.
O usuário pode digitar apenas uma letra por vez.
Se a letra estiver na palavra, ela será exibida.
Se não estiver, será exibido "*".
Também devemos contar o número de tentativas.
"""

# Importa o módulo random para escolher uma palavra aleatória
import os
import random

# Lista de palavras possíveis
palavras = ['python', 'celular', 'sistema', 'codigo', 'programador']

# Escolhe uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# String que vai armazenar as letras corretas que o usuário acertou
letras_acertadas = ''



# Contador de tentativas
tentativas = 0

# Loop infinito (o jogo só termina quando o usuário acertar)
while True:

    # Pede ao usuário uma letra
    # lower() -> transforma em minúscula
    # strip() -> remove espaços antes/depois
    letra_digitada = input('Digite uma letra: ').lower().strip()
    # Soma 1 tentativa
    tentativas += 1

    # Verifica se o usuário digitou apenas UMA letra válida
    if len(letra_digitada) != 1 or not letra_digitada.isalpha():
        print('❌ Digite apenas UMA letra válida.')
        continue  # volta para o início do loop

 

    # Verifica se a letra está na palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada  # adiciona letra correta

    # Variável que vai montar a palavra exibida (com letras ou *)
    palavra_formada = ''

    # Percorre cada letra da palavra secreta
    for letra in palavra_secreta:

        # Se a letra já foi acertada
        if letra in letras_acertadas:
            palavra_formada += letra  # mostra a letra
        else:
            palavra_formada += '*'  # mostra *

    # Mostra a palavra parcial
    print('Palavra:', palavra_formada)

    # Se a palavra formada for igual à palavra secreta, o usuário venceu
    if palavra_formada == palavra_secreta:        
        os.system('cls')
        print(f'🎉 Você descobriu a palavra em {tentativas} tentativas!')
        letras_acertadas = ''
        tentativas = 0
        palavra_secreta = random.choice(palavras)