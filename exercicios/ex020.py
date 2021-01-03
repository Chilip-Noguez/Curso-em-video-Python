from random import shuffle
alunos = []
for aluno in range(0, 4):
    alunos.append(input(f'Digite o nome do {aluno+1}º aluno: '))
shuffle(alunos)

print('A ordem de apresentação será:')
print(alunos)