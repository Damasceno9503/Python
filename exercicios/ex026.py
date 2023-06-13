frase = str(input('Digite uma frase: ')).strip().lower()
pri = frase.find('a') + 1
ult = frase.rfind('a') + 1
total = frase.count('a')
test = ('a' in frase.lower())
cores = {'limpo' : '\033[m',
         'amarelo' : '\033[33m',
         'azul' : '\033[34m',
         'roxo' : '\033[35m'}
print(f'A primeira letra A apareceu na posição {cores["amarelo"]}{pri}{cores["limpo"]}')
print(f'A letra A aparece {cores["azul"]}{total}{cores["limpo"]} vezes na frase.')
print(f'A ultima letra A apareceu na posição {cores["roxo"]}{ult}{cores["limpo"]}')