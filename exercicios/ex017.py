from math import hypot
c_oposto = float(input('Digite o cateto oposto: '))
c_adjacente = float(input('Digite o cateto adjacente: '))

hipot = (c_oposto**2 + c_adjacente**2)**0.5
hipotenusa = hypot(c_oposto, c_adjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipot))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
