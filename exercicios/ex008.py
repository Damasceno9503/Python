medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cores = {'limpa' : '\033[m',
         'brancoazul' : '\033[36;107m',
         'brancoamarelo' : '\033[33;107m',
         'vermelho' : '\033[31m',
         'roxo' : '\033[35m',
         'verde' : '\033[32m',
         'azul' : '\033[34m'}
print(f'A medida de {cores["brancoamarelo"]}{medida}m{cores["limpa"]} corresponde a {cores["verde"]}{cm:.0f}cm{cores["limpa"]} e {cores["vermelho"]}{mm:.0f}mm{cores["limpa"]}')
print(f'A medida de {cores["brancoazul"]}{km}km{cores["limpa"]}, a medida de {cores["azul"]}{hm}hm{cores["limpa"]}, a medida de {cores["roxo"]}{dam}dam{cores["limpa"]}, a medida de {cores["verde"]}{dm}dm{cores["limpa"]}.')
