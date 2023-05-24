nome = str(input('Diga Seu nome completo: ')).strip()
frase = nome
#frase = ('felipe valdinei santada de jesus')
print(f'Seu nome em maiúsculo é {frase.upper()}')
print(f'Seu nome em minúsculo é {frase.lower()}')
conta = frase.split(' ')
resultado = ''.join(conta)
print(f'Seu nome tem um total de {len(resultado)} letras')
print(f'Seu primeiro nome tem um total de {nome.find(" ")} Letras')