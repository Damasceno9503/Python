nome = str(input('Diga o nome da cidade que você nasceu: ')).strip()
r = (nome[:5].upper() == 'SANTO')
limpo = '\033[m'
amarelo = '\033[33m'
print(f'A cidade que você nasceu tem {amarelo}santos{limpo} no nome? {amarelo}{r}{limpo}')
