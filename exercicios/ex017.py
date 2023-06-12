from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)#
limpa = '\033[m'
amarelo = '\033[1;33;46m'
print(f'A hipotenusa vai medir {amarelo}{hi:.2f}{limpa}')