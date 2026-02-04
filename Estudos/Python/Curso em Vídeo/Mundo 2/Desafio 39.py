from datetime import date
from stat import FILE_ATTRIBUTE_DEVICE

nasc = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('está na hora de se alistar')
elif idade < 18:
    print('ainda não está na hora de se alistar, faltam {} anos'.format(18 - idade))
else:
    idade > 18
    print('passou do prazo de alistamento, seu período de alistamento foi há {} anos em {}'.format(idade - 18,nasc + 18))