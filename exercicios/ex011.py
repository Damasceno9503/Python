largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
metros = largura * altura
litros = metros / 2
limpa = '\033[m'
roxo = '\033[35m'
amarelo = '\033[33m'
azul = '\033[34m'
print(f'Sua parede tem dimensão de {amarelo}{largura}{limpa}x{amarelo}{altura}{limpa} e sua área  é de {azul}{metros}m²{limpa}.')
print(f'Para pintar essa parede, você precisará de {roxo}{litros}L{limpa} de tinta.')
