valor = float(input('Qual e o preço do produto: R$'))
desc = valor - (valor * 5 / 100)
limpa = '\033[m'
verde = '\033[32m'
print(f'O produto que custava {verde}R${valor:.2f}{limpa}, na promoção com desconto de 5% vai custar {verde}{desc:.2f}{limpa}')
