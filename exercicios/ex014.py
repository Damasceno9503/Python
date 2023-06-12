c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
limpa = '\033[m'
amarelo = '\033[33m'
azul = '\033[36m'
print(f'A temperatura de {azul}{c}ºC{limpa} corresponde a {amarelo}{f}ºF{limpa}!')