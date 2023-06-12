from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
limpa = '\033[m'
vermelha = '\033[1;31m'
shuffle(lista)
print(f'A ordem de apresentação será{vermelha}')
print(lista)
