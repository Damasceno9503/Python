from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
# lista = [a1, a2, a3, a4] #
# escolhido = choice(lista) #
prim = choice([a1, a2, a3, a4])
limpa = '\033[m'
amarelo = '\033[1;33m'
print(f'O aluno escolhido é {amarelo}{prim}{limpa}')
