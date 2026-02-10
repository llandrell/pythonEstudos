#Peça ao usuário para digitar seu nome (ok)
#peça ao usuário para digitar sua idade (ok)
#se nome e idade forem digitados: (ok)
# exiba:   
    # seu nome é {nome}(ok)
    # seu nome invertido é {nome invertido}(ok)
    # seu nome contém (ou não) espaços (ok)
    # seu nome tem {n} letras
    # a priomeira letra do seu nome é {letra} (ok)
    #a ultima letra do seu nome é {letra}
# se na for digitado em nome ou idade
    #exiba "Desculpe, você deixou campos vazios ou incorretos"(ok)



# entrada_nome_usuario = input("Informe seu nome: ").strip()
# entrada_idade_usuario = input("informe a sua idade em numneros, Ex: 32: ")

# try:

#     nome_usuario = entrada_nome_usuario.strip()
    
#     idade_usuario = int(entrada_idade_usuario)

#     print(f'Seu nome é {nome_usuario}')
#     print(f'Sua idade é {idade_usuario} anos')
#     print(f'Seu nome invertido é {nome_usuario[::-1]}')
#     if ' ' in nome_usuario:
#         print(f'seu nome: {nome_usuario}, contém espaços')
#     else: 
#         print(f'seu nome não contém espaços: {nome_usuario}')
#     nome_sem_espaco = nome_usuario.replace(" ","")
#     print(f'seu nome tem : {len(nome_sem_espaco)} letras')
#     print(f'A primeira letra do seu nome é: {nome_usuario[0]}')
#     print(f'A ultima letra do seu nome é : {nome_usuario[-1]}')


   
# except ValueError:

#     print("Desculpe, você deixou campos vazios ou digitou errado!")







nome_usuario = input("Informe seu nome: ").strip()
idade_usuario = input("Informe sua idade: ")

if not nome_usuario or not idade_usuario:
    print("Desculpe, você deixou campos vazios")
    exit()

try:
    idade_usuario = int(idade_usuario)
except ValueError:
    print("Idade inválida. Digite apenas números.")
    exit()

print(f"Seu nome é {nome_usuario}")
print(f"Sua idade é {idade_usuario} anos")
print(f"Seu nome invertido é {nome_usuario[::-1]}")

if ' ' in nome_usuario:
    print("Seu nome contém espaços")
else:
    print("Seu nome não contém espaços")

nome_sem_espacos = nome_usuario.replace(" ", "")
print(f"Seu nome tem {len(nome_sem_espacos)} letras")

print(f"A primeira letra do seu nome é: {nome_usuario[0]}")
print(f"A última letra do seu nome é: {nome_usuario[-1]}")