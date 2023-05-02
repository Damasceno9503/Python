largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
metros = largura * altura
litros = metros / 2
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área  é de {metros}m².')
print(f'Para pintar essa parede, você precisará de {litros}L de tinta.')
