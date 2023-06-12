nome = str(input('Diga Seu nome completo: ')).strip()
frase = nome
#frase = ('felipe valdinei santada de jesus')
cores = {'limpa' : '\033[m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[4;31m'}
print(f'Seu nome em maiúsculo é {cores["amarelo"]}{frase.upper()}{cores["limpa"]}')
print(f'Seu nome em minúsculo é {cores["amarelo"]}{frase.lower()}{cores["limpa"]}')
conta = frase.split(' ')
resultado = ''.join(conta)
print(f'Seu nome tem um total de {cores["vermelho"]}{len(resultado)}{cores["limpa"]} letras')
print(f'Seu primeiro nome tem um total de {cores["vermelho"]}{nome.find(" ")}{cores["limpa"]} Letras')