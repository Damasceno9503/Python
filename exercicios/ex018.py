from math import radians, sin, cos, tan 
angulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(angulo))
limpa = '\033[m'
vermelho = '\033[1;31;47m'
amarelo = '\033[4;33m'
verde = '\033[1;32;47m'
roxo = '\033[1;35;47m'
print(f'O ângulo de {amarelo}{angulo}{limpa} tem o SENO de {vermelho}{seno:.2f}{limpa}')
cosseno = cos(radians(angulo))
print(f'O ãngulo de {amarelo}{angulo}{limpa} tem o COSSENO de {verde}{cosseno:.2f}{limpa}')
tangente = tan(radians(angulo))
print(f'O ãngulo de {amarelo}{angulo}{limpa} tem o TANGENTE de {roxo}{tangente:.2f}{limpa}')
