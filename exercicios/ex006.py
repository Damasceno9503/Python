n1 = int(input('Diga um número: '))
m = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
cores = {'limpa' : '\033[m',
        'preto' : '\033[97;40m',
        'roxo' : '\033[35m',
        'amarelo' : '\033[33m',
        'azul' : '\033[34m'}
print(f'O dobro de {cores["preto"]}{n1}{cores["limpa"]} vale {cores["amarelo"]}{m}{cores["limpa"]}.')
print(f'o triplo de {cores["preto"]}{n1}{cores["limpa"]} vale {cores["azul"]}{t}{cores["limpa"]}.')
print(f'A raiz quadrada de {cores["preto"]}{n1}{cores["limpa"]} é igual a {cores["roxo"]}{r:.3}{cores["limpa"]}.')
