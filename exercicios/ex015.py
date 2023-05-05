Km = float(input('Quantos Km você andou? '))
dias = int(input('Quantos dias você ficou com o carro? '))
n1 = Km * 0.15
n2 = dias * 60
total = n1 + n2
print(f'Você deve pagar R${total:.2f}')