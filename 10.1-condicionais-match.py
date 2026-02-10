entrada =  input("Entrar, login, acessar ou sair? ")

# O 'match' recebe o objeto que queremos analisar (o 'alvo')
match entrada:
    
    # O case "entrar" | "login" | "acessar":
    # O símbolo '|' funciona como um "OU" (OR).
    # O Python verifica: "entrada" é IGUAL a "entrar" OU "login" OU "acessar"?
    case "entrar" | "login" | "acessar":
        print("Iniciando sessão...")

    # Se a primeira tentativa falhar, ele testa este próximo padrão.
    case "sair" | "logout":
        print("Saindo...")

    # O case _: é o nosso "curinga" (wildcard).
    # Ele captura qualquer coisa que não tenha sido "casada" nos blocos anteriores.
    # É o equivalente exato ao 'else'.
    case _:
        print("Comando desconhecido.")

'''
DIFERENÇA DE IF PARA MATCH:

No 'if', precisamos repetir o nome da variável e o operador '==' várias vezes
if entrada == "entrar" or entrada == "login" or entrada == "acessar":
    print("Iniciando sessão...")
elif entrada == "sair" or entrada == "logout":
    print("Saindo...")
else:
    print("Comando desconhecido.")

    
# COMPARAÇÃO: IF/ELIF/ELSE vs MATCH/CASE

# 1. PODER DE DECISÃO
# IF: Baseado em condições booleanas (True/False) gerais.
# MATCH: Baseado em padrões (igualdade, tipos e estruturas).

# 2. SINTAXE
# IF: Requer repetir a variável ou usar 'in' para múltiplos valores.
# MATCH: Mais limpo, utiliza o pipe (|) para agrupar opções.

# 3. LEGIBILIDADE
# IF: Pode ficar poluído quando existem muitas condições 'or'.
# MATCH: Muito mais organizado para menus e listas de comandos.

# 4. USO DE MEMÓRIA
# IF: Avalia cada condição uma por uma, de forma sequencial.
# MATCH: Otimizado pelo interpretador para encontrar o caso correto mais rápido.    
    
'''



# EXPLICAÇÃO: LÓGICA "AND" NO MATCH/CASE (USANDO GUARDS)


# 1. No Python, usamos a palavra 'and' em vez de '&&'.
# 2. Dentro do 'match', a checagem "E" é feita com um 'if' após o padrão.
#    Isso é chamado de "Guard" (Guarda).

status_usuario = "admin"
tentativas_login = 3

match status_usuario:
    # Caso seja "admin" E (if) as tentativas forem maiores que 2:
    case "admin" if tentativas_login > 2:
        print("ALERTA: Administrador com múltiplas tentativas de login!")

    # Caso seja "admin" E (if) as tentativas forem poucas:
    case "admin" if tentativas_login <= 2:
        print("Acesso administrativo liberado.")

    # Caso padrão (else)
    case _:
        print("Usuário comum ou dados inválidos.")

# 
# EXEMPLO 2: Comparando múltiplos valores ao mesmo tempo (Tuplas)
# Esta é outra forma potente de fazer o "AND" estruturalmente.
# 

comando = "deletar"
confirmacao = True

# Aqui o match olha para os dois valores ao mesmo tempo
match (comando, confirmacao):
    # Só entra se o primeiro for "deletar" E o segundo for True
    case ("deletar", True):
        print("Arquivo excluído com sucesso.")

    # Só entra se o primeiro for "deletar" E o segundo for False
    case ("deletar", False):
        print("Operação de exclusão cancelada pelo usuário.")

    case _:
        print("Comando não reconhecido.")

# 
# RESUMO DA SINTAXE:
# case [padrão] if [condição_and_1] and [condição_and_2]:
# 