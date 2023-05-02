valor = float(input('Qual e o preço do produto: R$'))
desc = valor - (valor * 5 / 100)
print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar {desc:.2f}')
