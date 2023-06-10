v = float(input('Quantos reais voçê tem? R$'))
t = v / 5.03
verde = '\033[32m'
limpo = '\033[m'
print(f'Com {verde}R${v:.2f}{limpo} você pode comprar {verde}US${t:.2f}{limpo}')
