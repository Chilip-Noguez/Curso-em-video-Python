city = str(input("Digite o nome da cidade: ")).strip().capitalize().split()

city_split = bool('Santo' in city[0])
print('O nome da cidade começa com Santo? {}'.format(city_split))
