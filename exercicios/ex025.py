nome = str(input('Qual é seu nome? ')).strip()
r = ('silva'in nome.lower())
limpo = '\033[m'
amarelo = '\033[33m'
print(f'Seu nome tem {amarelo}silva{limpo} no nome? {amarelo}{r}{limpo}')
