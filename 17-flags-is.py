#Flag (Bandeira) - Marcar um local
#Uma flag é uma variável usada para indicar se algo aconteceu ou não.
#None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)

# Flag (Bandeira) - indica se entrou no if
condicao = True
passou_no_if = False  # começamos assumindo que não passou

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# Verificação da flag
if passou_no_if:
    print('Passou no if')
else:
    print('Não passou no if')



'''
Use True/False para flags simples.

Use None quando quer indicar “ainda não definido”.

Use is None para checar None.

Simplifique sempre que possível.

'''


'''
exemplos:

usuario_logado = None

usuario = input("Digite seu usuário: ")

if usuario == "andre":
    usuario_logado = True
    print("Login realizado com sucesso!")
else:
    print("Usuário incorreto")

if usuario_logado is None:
    print("Nenhum login válido foi realizado.")
else:
    print("Usuário autenticado.")




'''