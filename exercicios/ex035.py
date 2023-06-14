print('\033[33m-=\033[m' * 20 ) 
print('Analisandor de Triângulos')
print('\033[33m-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
limpo = '\033[m'
verde = '\033[32m'
vermelho = '\033[31m'
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'{verde}Os segmentos acima PODEM FORMAR triângulos!{limpo}')
else:
    print(f'{vermelho}Os segmentos Acima NÃO PODEM FORMAR triângulos!{limpo}')
