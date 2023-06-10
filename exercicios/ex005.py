n1 = int(input('Diga um número: '))
nmenos = int(n1 - 1,)
nmais = int(n1 + 1)
amarelo = '\033[33m'
azulclaro = '\033[36m'
azulescuro = '\033[34m'
normal = '\033[m'
print(f'o antecessor do número {amarelo}{n1}{normal} e {azulclaro}{nmenos}{normal} o seu sucessor e {azulescuro}{nmais}{normal}')
