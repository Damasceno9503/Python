frase = str(input('Digite uma frase: ')).strip().lower()
pri = frase[:1].find('a') + 1
ult = frase.rfind('a') + 1
total = frase.count('a')
test = ('a' in frase.lower())

print(f'A primeira letra A apareceu na posição {pri}')
print(f'A letra A aparece {total} vezes na frase.') 
print(f'A ultima letra A apareceu na posição {ult}')