from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
# lista = [a1, a2, a3, a4] #
# escolhido = choice(lista) #
prim = choice([a1, a2, a3, a4])
print(f'O aluno escolhido é {prim}')
