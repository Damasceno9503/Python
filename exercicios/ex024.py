nome = str(input('Diga o nome da cidade que você nasceu: ')).strip()
r = (nome[:5].upper() == 'SANTO')
print(f'A cidade que você nasceu tem santos no nome? {r}')