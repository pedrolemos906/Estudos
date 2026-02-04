v = float(input('informe a distacia da viagem: '))
if v <= 200:
    valor1 = v * 0.50
    print('sua viagem vai custar R${:.2f}'.format(valor1))
else:
    valor2 = v * 0.45
    print('sua viagem vai custar R${:.2f}'.format(valor2))
