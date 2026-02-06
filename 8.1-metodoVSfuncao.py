# FUNÇÃO = Independente (chama com nome())
def gritar(texto):        # Função global
    return print(texto.upper())

# MÉTODO = Função "grudada" no objeto (chama com .)
texto = "python"

gritar(texto)           # ✅ FUNÇÃO recebe objeto
print(texto.upper())           # ✅ MÉTODO do objeto texto

# Diferença visual:
print(len(texto))       # FUNÇÃO
print(texto.__len__())  # MESMA coisa, mas como MÉTODO!