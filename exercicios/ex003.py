n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
cor1 = '\033[35m'
cor2 = '\033[33m'
cor3 = '\033[0;33;45m'
normal = '\033[m'
print(f'A soma entre {cor1}{n1}{normal} e {cor2}{n2}{normal} é igual a {cor3}{s}{normal}!')
