from random import randint
from time import sleep
computador = randint(0,5)
print('penseino numero')
print("-=-"*20)
print('vou pensar em um numero entre 0 e 5. Tente adivinhar...' )
print('-=-'*20)
jogador = int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('parabens!')
else:
    print('vc errou')