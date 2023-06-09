print('\033[30;107m-=\033[m' * 20 ) 
print('Analisandor de Triângulos')
print('\033[30;107m-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos Acima NÃO PODEM FORMAR triângulos!')
