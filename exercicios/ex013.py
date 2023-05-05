valor = float(input('Qual e o salário do funcionario? R$'))
aum = valor + (valor * 15/100)
print(f'O funcionário ganhava R${valor:.2f}, com 15% de aumento, passa a receber R${aum:.2f}')