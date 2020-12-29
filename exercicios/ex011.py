largura = float(input('Entre com a largura da parede: '))
altura = float(input('Entre com a altura da parede: '))

area = largura * altura
tinta = area / 2
print('A dimensão da parede {}x{} e tem a área de: {}m²'.format(largura, altura, area))
print('A quantidade de litros necessários é: {:.4f}l'.format(tinta))