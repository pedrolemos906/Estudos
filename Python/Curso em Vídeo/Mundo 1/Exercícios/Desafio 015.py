dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
valordias = dias * 60
valorkm= km * 0.15
valortotal = valordias + valorkm
print('o valor a ser pago é de R${:.2f}!'.format(valortotal))

