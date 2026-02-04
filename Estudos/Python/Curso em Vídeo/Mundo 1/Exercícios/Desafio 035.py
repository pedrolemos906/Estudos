#input
seg1 = float(input('informe o valor da primeira reta: '))
seg2 = float(input('informe o valor da segunda reta: '))
seg3 = float(input('informe o valor da terceira reta: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 <  seg1 + seg2:
    print('esses valores formam um triangulo')
else:
    print('esses valores não formam um triangulo')