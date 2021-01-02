km_rodado = float(input('Digite a quantidade de Km percorridos: '))
q_dias = int(input('Digite a quantidade de dias de locação: '))

valor_km = km_rodado * 0.15
valor_dias = q_dias * 60
total = valor_dias + valor_km

print('O valor para os KMs rodados {}: R$ {}'.format(km_rodado, valor_km))
print('O valor total das diárias {}: R$ {}'.format(q_dias, valor_dias))
print('O valor total: {}'.format(total))