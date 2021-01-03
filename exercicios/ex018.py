import math
angulo = float(input('Digite o angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Para o angulo {}, o seno é {:.2f}, \no cosseno é {:.2f} \ne a tangente é {:.2f}!'.format(angulo, seno, cosseno, tangente))
