num = int (input('digite um numero: '))
print('''escolha uma das opcoes abaixo:
digite 1 para binario
digite 2 para octal 
digite 3 para hexadecimal ''')

sistema = int(input('escolha: '))

if sistema == 1:
    print('{} em binario é {}'.format(num, bin(num)[2:]))

elif sistema == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))
elif sistema == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida, tente novamente')

