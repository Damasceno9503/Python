nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome legal!')
else:
    print('Seu nome e muito comum!')
print(f'Bom dia, {nome}')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
#if m >= 6.0:
    #print('Voce tem uma boa nota.Parabens!')
#else:
    #print('voce tem uma pessima nota. Estude mais!')
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')