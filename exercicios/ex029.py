velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
limpa = '\033[m'
verde = '\033[1;32m'
vermelho = '\033[31m'
if velocidade > 80:
    print(f'{vermelho}Multado! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!{limpa}')
else:
    print(f'{verde}Tenha um bom dia! Dirija com segurança!{limpa}')
