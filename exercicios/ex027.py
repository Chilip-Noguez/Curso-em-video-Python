nome = str(input('Digite seu nome completo: ')).strip()

nome_split = nome.split()
print('O primeiro nome é {}'.format(nome_split[0]))
print('O último nome é {}'.format(nome_split[-1]))
