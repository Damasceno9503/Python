Km = float(input('Quantos Km você andou? '))
dias = int(input('Quantos dias você ficou com o carro? '))
n1 = Km * 0.15
n2 = dias * 60
total = n1 + n2
limpo = '\033[m'
verde = '\033[32m'
print(f'Você deve pagar {verde}R${total:.2f}{limpo}')