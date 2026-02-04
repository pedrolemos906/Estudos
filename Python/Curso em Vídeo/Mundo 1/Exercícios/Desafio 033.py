#input
n1 = int(input('informe o primeiro valor: '))
n2 = int(input('informe o segundo valor: '))
n3 = int(input('informe o terceiro valor: '))

#verificacao do maior numero
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#verificacao do menor numero
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#resultado
print('o maior numero é: {}'.format(maior))
print('o menor numero é: {}'.format(menor))
