salario = float(input('Entre com o salário: '))
novo_sal = salario + (salario * 0.15)
print('O salário de {:.2f}, com 15% de aumento, agora é R${:.2f}'.format(salario, novo_sal))