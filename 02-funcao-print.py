
# ========================================
# Função print() - Parâmetros SEP e END
# ========================================

# 1. PRINT BÁSICO - Um único argumento
print('Exibe no prompt, a função print recebe argumentos')
# Resultado: Exibe exatamente o texto entre aspas

# 2. PARÂMETRO SEP - Controla o SEPARADOR entre múltiplos argumentos
# Padrão: espaço simples " "
print('é possível mudar o separador da função print exemplo:...', 10, 11, "outro texto", sep="-")
# Resultado: é possível mudar o separador da função print exemplo:...-10-11-outro texto

# 3. PARÂMETRO END - Controla o FINAL da linha (quebra ou não)
# Padrão: "\n" (nova linha)
print('é possível mudar a quebra de linha também', end="")  # Sem quebra
print(' <- Mesma linha!')  # Continua na mesma linha

# 4. COMBINANDO SEP + END - Controle total
print('Números:', 100, 200, 300, sep=" | ", end=" -> ")
print('Fim da sequência!')

# 5. EXEMPLOS PRÁTICOS
print("\n=== BARRAS DE PROGRESSO ===")
for i in range(5):
    print(".", end="", flush=True)  # flush=True força exibição imediata
print(" Concluído!")

print("\n=== COORDENADAS GPS ===")
lat, lon = -12.9711, -38.5108  # Matatu, Bahia
print("Localização:", lat, "°N", lon, "°W", sep=" | ")

print("\n=== TIPOS DIFERENTES ===")
nome = "André"
idade = 25
saldo = 150.50
print(nome, idade, "anos", f"R$ {saldo:.2f}", sep=" → ")