primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

try:
    numero1 = int(primeiro_valor.strip())  # .strip() remove espaços
    numero2 = int(segundo_valor.strip())   # evita erro com espaços extras
    
  
    if numero1 > numero2:
        print(f'✅ PRIMEIRO ({numero1}) é MAIOR que SEGUNDO ({numero2})')
    elif numero2 > numero1:
        print(f'✅ SEGUNDO ({numero2}) é MAIOR que PRIMEIRO ({numero1})')
    else:  # numero1 == numero2
        print(f'⚖️ PRIMEIRO ({numero1}) é IGUAL ao SEGUNDO ({numero2})')
        
except ValueError:
    print("❌ Erro: Digite apenas números inteiros válidos!")