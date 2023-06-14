limpo = '\033[m'
verde = '\033[32m'
amarelo = '\033[33m'
distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {amarelo}{distância}Km{limpo}.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de {verde}R${preço:.2f}{limpo}')
'''promocao = viagem * 0.45
valor = viagem * 0.50
if viagem >= 200:
    print(f'Você está preste a começar uma viagem de {viagem:.1f}Km\nE o preço da sua passagem na promoção será de R${promocao:.2f}')
else:
    print(f'Você está preste a começar uma viagem de {viagem:.1f}Km\nE o preço da sua passagem será de R${valor:.2f}')'''
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}.')'''