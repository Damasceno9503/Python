#5+3*2 == 11
#3*5+4**2 == 31
#3*(5+4)**2 == 243

#-1 () 
#-2 ** 
#-3 * / // % 
#-4 + - 

#nome = input('Qual é seu nome? ')
#print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
cores = {'limpa' : '\033[m',
         'vermelho' : '\033[31m',
         'amarelo' : '\033[33m',
         'verde' : '\033[32m',
         'roxo' : '\033[35m',
         'azul' : '\033[36m'}
print(f'A soma é {cores["amarelo"]}{s}{cores["limpa"]}, o produto é {cores["verde"]}{m}{cores["limpa"]} e a divisão é {cores["vermelho"]}{d:.3f}{cores["limpa"]}', end=' ')
print(f'Divisão inteira {cores["azul"]}{di}{cores["limpa"]} e potência {cores["roxo"]}{e}{cores["limpa"]}')
