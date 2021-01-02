import math
from math import sqrt, floor
from math import ceil as topo
import random

# num = int(input('Digite um numero: '))
num = 91
raiz = math.sqrt(num) #utilizando o import
print('A raiz quadrada de {} é igual a {}.'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é igual a {}.'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} é igual a {}.'.format(num, math.sqrt(num)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, raiz))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, floor(raiz))) #utilizando from import
print('Raiz qudrada utilizndo topo: {}'.format(topo(num)))

print('#'*44)

n = random.random()
print(n)
print(random.random())
n_int = random.randint(1, 50) #número aleatório entre 'a' e 'b'
print(n_int)