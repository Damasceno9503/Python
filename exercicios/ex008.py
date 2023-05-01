medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10

print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')
print(f'A medida de {km}km, a medida de {hm}hm, a medida de {dam}dam, a medida de {dm}dm.')
