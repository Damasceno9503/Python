from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
limpo = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{verde}O ano {ano} é BISSEXTO{limpo}')
else:
    print(f'{vermelho}o ano {ano} NÃO é BISSEXTO{limpo}')
