n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
Cores = {'limpa' : '\033[m',
         'cinza' : '\033[37;107m',
         'verde' : '\033[32m',
         'azul' : '\033[36m'}
print(f'A média entre {Cores["verde"]}{n1:.1f}{Cores["limpa"]} e {Cores["azul"]}{n2:.1f}{Cores["limpa"]} é igual a {Cores["cinza"]}{m:.1f}{Cores["limpa"]}')
