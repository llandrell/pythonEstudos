import locale

# Configura para padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# f-string (simples e limpa)

nome = "Lucas"
idade = 32
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

nome = "André"
altura = 1.80
peso = 88

# Cálculos diretos
print(f"IMC do {nome}: {peso / (altura ** 2):.2f}")

# Funções e métodos
print(f"Nome em maiúscula: {nome.upper()}")
print(f"Tamanho do nome: {len(nome)} letras")


preco = 1234.5678
quantidade = 42

print(f"Preço unitário: R$ {preco:.2f}")           # 2 casas decimais
print(f"Total: R$ {preco * quantidade:n}")      # Separa milhar
print(f"Preço com 4 casas: R$ {preco:.4f}")        # 4 casas decimais
print(f"Inteiro alinhado: {quantidade:03d}")       # 3 dígitos (preenche com 0)