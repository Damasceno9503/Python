from random import randint
print('-=-' *20)
str(print('Vou pensar em um número entre 0 e 5. tente adivinhar...'))
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) #numero q o jogador pensa
computador = randint(0, 5) #numero q o computador pensa
if jogador == computador:
    print('PARABÉNS! voce ganhou de mim!')
    print('=' *60)
else:
    print(f'EU GANHEI! eu pensei no número {computador} e não no {jogador}!')
    print('=' *60)