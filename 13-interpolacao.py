# =====================================================
# INTERPOLAÇÃO DE STRINGS COM %
# =====================================================

# Placeholders mais comuns:
# %s → string
# %d ou %i → inteiro
# %f → float
# %x ou %X → hexadecimal

nome = "Luiz"
preco = 10000.9897979

# %.2f → float com 2 casas decimais
variavel = '%s, o preço total foi de R$: %.2f' % (nome, preco)
print(variavel)

# %08x → hexadecimal com 8 dígitos, preenchido com zero à esquerda
print('O hexadecimal de %d é %08x' % (32, 32))


# =====================================================
# INTERPOLAÇÃO COM .format()
# =====================================================

nome = "Luiz"
preco = 10000.9897979

texto = "{}, o preço total foi de R$: {:.2f}".format(nome, preco)
print(texto)

# Com índices (menos comum hoje)
texto = "{0}, o preço total foi de R$: {1:.2f}".format(nome, preco)
print(texto)

# Com nomes (mais legível)
texto = "{nome}, o preço total foi de R$: {preco:.2f}".format(
    nome=nome,
    preco=preco
)
print(texto)



# =====================================================
# f-strings (FORMA MODERNA E RECOMENDADA)
# =====================================================

nome = "Luiz"
preco = 10000.9897979

texto = f"{nome}, o preço total foi de R$: {preco:.2f}"
print(texto)