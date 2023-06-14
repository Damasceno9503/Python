n = int(input('Me diga um número qualquer: '))
mult = n % 2
limpo = '\033[m'
vermelho = '\033[31m'
roxo = '\033[35m'
amarelo = '\033[33m'
if mult == 0:
    print(f'{amarelo}O número {n} é {roxo}PAR{limpo}{amarelo}.{limpo}')
else:
    print(f'{amarelo}O numero {n} é {vermelho}ÍMPAR{limpo}{amarelo}.{limpo}')