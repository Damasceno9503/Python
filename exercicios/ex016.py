from math import trunc
num = float(input('Digite um numero com pontos flutuantes: '))
por = trunc(num)
limpa = '\033[m'
vermelho = '\033[31;107m'
roxo = '\033[35;107m'
print(f'O valor digitado foi {roxo}{num}{limpa} e a sua porção inteira é {vermelho}{por}{limpa}')
'''num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int}')'''
