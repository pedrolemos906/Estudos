#input
salario = float(input('informe o salario atual: '))

#condicoes
if salario > 1250:
    aumento = salario * 0.10

else:
    aumento = salario * 0.15

#resultado
print('o aumento foi de R${} e o funcionario passará a receber R${}.'.format(aumento,salario + aumento))
