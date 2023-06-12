valor = float(input('Qual e o salário do funcionario? R$'))
aum = valor + (valor * 15/100)
limpa = '\033[m'
verde = '\033[32m'
print(f'O funcionário ganhava {verde}R${valor:.2f}{limpa}, com 15% de aumento, passa a receber {verde}R${aum:.2f}{limpa}')