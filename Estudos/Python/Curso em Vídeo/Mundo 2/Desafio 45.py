from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print('''escolha uma opcao abaixo:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('qual a sua opcao? '))

if jogador != 0 and jogador != 1 and jogador != 2:
    print('escolha uma das opcoes validas, seu idiota!')


else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-=-' * 10)
    print('computador jogou {}'.format(itens[computador]))
    print('jogador jogou {}'.format(itens[jogador]))
    print('-=-' * 10)

    if computador == 0:
        if jogador == 0:
            print('empate')
        elif jogador == 1:
            print('jogador ganhou')
        else:
            jogador == 2
            print('computador ganhou')


    elif computador == 1:
        if jogador == 0:
            print('computador ganhou')
        elif jogador == 1:
            print('empate')
        else:
            jogador == 2
            print('jogador ganhou')


    else:
        computador == 2
        if jogador == 0:
            print('jogador ganhou')
        elif jogador == 1:
            print('computador ganhou')
        else:
            jogador == 2
            print('empate')

