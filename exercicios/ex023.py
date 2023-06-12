num = int(input('informe um número de 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
cores = {'limpa' : '\033[m',
         'branco' : '\033[7m',
         'verde' : '\033[1;32m',
         'amarelo' : '\033[1;33m',
         'azul' : '\033[1;36m',
         'roxo' : '\033[1;35m'}
print(f'Analisando o número {cores["branco"]}{num}{cores["limpa"]}')
print(f'Unidade: {cores["verde"]}{u}{cores["limpa"]}')
print(f'Dezena: {cores["amarelo"]}{d}{cores["limpa"]}')
print(f'Centena: {cores["azul"]}{c}{cores["limpa"]}')
print(f'Milhar: {cores["roxo"]}{m}{cores["limpa"]}')
