from random import choice
alunos = []
for aluno in range(0, 4):
    alunos.append(input(f'Digite o nome do {aluno+1}º aluno: '))
print(alunos)

escolhido = choice(alunos)

print('O aluno escolhido foi: {}'.format(escolhido))