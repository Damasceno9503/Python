from random import randint
from time import sleep
cores = {'vermelho' : '\033[31m',
         'amarelo' : '\033[33m',
         'limpa' : '\033[m',
         'verde' : '\033[32m'}
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' *20)
str(print('Vou pensar em um número entre 0 e 5. tente adivinhar...'))
print(f'{cores["amarelo"]}-=-{cores["limpa"]}' *20)
jogador = int(input('Em que número eu pensei? ')) #numero q o jogador pensa
computador = randint(0, 5) #numero q o computador pensa
print(f'{cores["amarelo"]}PROCESSANDO...{cores["limpa"]}')
sleep(2)
if jogador == computador:
    print(f'{cores["verde"]}PARABÉNS! voce ganhou de mim!{cores["limpa"]}')
    print('=' *60)
else:
    print(f'{cores["vermelho"]}EU GANHEI! eu pensei no número {computador} e não no {jogador}!{cores["limpa"]}')
    print(f'{cores["amarelo"]}={cores["limpa"]}' *60)