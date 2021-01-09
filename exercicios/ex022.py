nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
nome_split = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome_split[0])))