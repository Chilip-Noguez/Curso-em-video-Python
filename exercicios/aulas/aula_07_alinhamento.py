nome = str(input('Digite seu nome: '))
print('É um prazer te conhecer, {:20}!'.format(nome)) #impressão com 20 caracteres

print('É um prazer te conhecer, {:>20}!'.format(nome)) #impressão de alinhamento à direita com 20 caracteres

print('É um prazer te conhecer, {:<20}!'.format(nome))#impressão de alinhamento à esquerda com 20 caracteres

print('É um prazer te conhecer, {:^20}!'.format(nome))#impressão de alinhamento centralizado com 20 caracteres

print('É um prazer te conhecer, {:=^20}!'.format(nome))#impressão de alinhamento centralizado com 20 caracteres
