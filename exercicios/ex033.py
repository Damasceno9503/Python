a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
limpo = '\033[m'
azul = '\033[34m'
roxo = '\033[35m'
print(f'O menor valor digitado foi {azul}{menor}{limpo}')
print(f'O maior valor digitado foi {roxo}{maior}{limpo}')