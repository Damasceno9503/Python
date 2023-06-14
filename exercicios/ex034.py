salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
limpo = '\033[m'
verde = '\033[32m'
print(f'Quem ganhava {verde}R${salario:.2f}{limpo} passa a ganhar {verde}R${aumento:.2f}{limpo} agora')
