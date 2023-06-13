nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
limpo = '\033[m'
verde = '\033[m'
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')