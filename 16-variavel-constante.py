#Constate = "Variavel" que não vai mudar de acordo com o codigo rodando
# no python não existe o conceito de constante, existe boas praticas
#
#muitas condições no mesmo if (ruim)
#
#   <--- quanto mais o codigo estiver afastado da margens e ruim
# ou sejá codigo dentro de codigo
# boas praticas para escrever condigo limpo
#

velocidade = 61  # Velocidade atual do carro
local_carro = 100  # Km onde o carro está

# Configuração do radar
LIMITE_RADAR = 60  #60km por hora
LOCAL_RADAR = 100 # km 100
RADAR_RANGE = 1  # Alcance de 1km para cada lado

# Verifica se o carro está dentro da área de alcance do radar
dentro_da_area = abs(local_carro - LOCAL_RADAR) <= RADAR_RANGE #abs transforma em numero absoluto, ou sejá
# -1 vira 1

print(f'{dentro_da_area=}') #retorna true pq <= é um comparador logico

# Verifica se deve multar
if velocidade > LIMITE_RADAR and dentro_da_area:
    print("Carro multado")
else:
    print("Carro não foi multado")





# id = Identidade

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
#2 variaveis diferentes no mesmo endereço de mememoria pq o python tenta ser eficiente.