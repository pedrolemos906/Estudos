v = int(input('Qual a velocidade atual do carro? '))
if v > 80:
    m = (v - 80) * 7
    print('voce foi multado! O valor da multa é de R${:.2f}.'.format(m))

print('tenha um bom dia!')