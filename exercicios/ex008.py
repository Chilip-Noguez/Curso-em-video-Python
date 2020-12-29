medida = float(input('Digite a quantidade de metros: '))
centimetros = medida * 100
milimetro = medida * 1000

print('{:.2f} metros é equivalente à {:.0f} centímetros e {:.0f} milimetros!'.format(medida, centimetros, milimetro))