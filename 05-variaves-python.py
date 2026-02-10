"""
5-variaveis-python

Variáveis em Python: São identificadores (apelidos) que referenciam objetos na memória.
Elas armazenam valores mutáveis ou imutáveis, permitindo reutilização e manipulação de dados.

Princípios do Clean Code (Robert C. Martin) aplicados:
- Nomes intencionalmente descritivos: Revelem o propósito da variável (evite abreviações como 'n' ou 'id'; prefira full_name).
- snake_case (PEP 8): minúsculas + underscores para variáveis.
- Uma única responsabilidade: Cada variável guarda um conceito claro.
- Evite mágica: Use nomes que expliquem o 'por quê', não só o 'o quê'.
- Constância: Para valores fixos (ex: IDADE_MINIMA_MAIORIDADE = 18), use UPPER_SNAKE_CASE.

Operador de atribuição '=': Associa o valor à variável (não é igualdade matemática).
Atualizações são baratas; nomes ruins custam caro em manutenção.

Exemplo prático: Dados pessoais para verificação de maioridade.
"""

# Dados pessoais (nomes descritivos revelam intenção)
primeiro_nome = "André"
nome_completo = f"{primeiro_nome} Lucas Almeida de Jesus"  # f-string para clareza (Python 3.6+)
idade_anual = 32  # Evite 'idade'; especifique unidade se relevante
IDADE_MINIMA_MAIORIDADE = 18  # Constante: UPPER_CASE, valor imutável

# Lógica simples e legível (uma linha por afirmação)
e_maior_de_idade = idade_anual >= IDADE_MINIMA_MAIORIDADE

# Saídas formatadas com f-strings (mais limpas que concatenação)
print(f"Nome completo: {nome_completo}")
print(f"Idade: {idade_anual} anos")
print(f"É maior de idade? {e_maior_de_idade}")  # True/False direto

# Boas práticas extras (Clean Code + PEP8):
# - Limite escopo: Declare variáveis perto do uso.
# - Evite reutilização: my_var = 5; my_var = "texto" confunde.
# - Tipagem (opcional, mas clara): idade_anual: int = 32
# Para seu negócio de consertos (Bahia): cliente_nome = "João"; orcamento_total = 150.50