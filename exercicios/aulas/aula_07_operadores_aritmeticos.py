"""
ORDEM DE ORESCEDENCIA
()
**
*  / // %
- +
"""
print(5+3*2)
print(5**2)
print(5**3)
print(19//2)
print(19//2)
#print(365**522)
print(18%2)
print(122%3)
print(4**3)
print(pow(4,3))
print(81**0.5) #calcular raiz quadrada
print(25**(1/2)) #calcular raiz quadrada
print(127**(1/3)) #calcular raiz cubica
print(1/3)
print('='*20)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro: "))
s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divisão inteira
e = n1 ** n2 #exponenciação
print('A soma é {}, \no produto é {}, e a \ndivisão é {:.3f}'.format(s, m, d), end=' ')
print('A duvisão é {} e a potencia é {}'.format(di, e))
