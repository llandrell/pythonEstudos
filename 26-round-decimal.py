'''
trabalahndo com imprecisões de pontos flutuantes em python
double-precision floatting-point

'''
import decimal

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')
num3 = num1 + num2
print(num3)
print(f'{num3:.2f}')#forma de contonar esse bug

#       
round(num3, 2)
print(num3)
print(f'{num3:.2f}')#forma de contonar esse bug

#usando a função round
print(round(num3, 2))

#ultilizando modulo de python decimla