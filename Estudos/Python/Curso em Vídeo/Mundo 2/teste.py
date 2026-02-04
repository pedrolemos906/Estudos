from random import randint

while True:
    ip = int(input('''digite:
    1 pra impar
    2 pra par
    qual a sua opcão: '''))
    if ip != 1 and ip != 2:
        print('opcao invalida')
        break
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'jogador jogou {jogador} e computador jogou {computador} e soma deu {soma}')
    if ip == 1 and soma % 2 != 0:
        print('jogador venceu!')
    elif ip == 2 and soma % 2 == 0:
        print('jogador venceu!')
    else:
      y  print('jogador perdeu!')