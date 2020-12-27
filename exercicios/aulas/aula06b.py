n = float(input('Digite um valor: '))
n_1 = bool(input('Digite um valor'))
n_2 = bool()
n_3 = '4'
n_4 = 'a1'
n_5 = 'asdasd'

texto = 'Hello World!'
print(n, 'é um inteiro: ', n.is_integer())
print(n_3.isnumeric())
print(n_1, type(n_1))
print(n_2, type(n_2))
print(texto, type(texto), texto.isnumeric())
print(f'O "{n_4}" é alfabeto? {n_4.isalpha()}')
print(f'O "{n_4}" é alfabeto? {n_4.isalnum()}')
print(f'O "{n_5}" é alfabeto? {n_5.isalpha()}')
print(f'O "{n_5}" é alfabeto? {n_5.isalnum()}')