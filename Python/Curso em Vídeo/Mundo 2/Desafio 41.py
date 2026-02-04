from datetime import date
nasc = int(input('digite o ano de nascimento do atleta: '))
idade =  date.today().year - nasc
if idade <= 9:
    print('o ateleta com idade de {} anos está na categoria MIRIM. '.format(idade))
elif idade > 9 and idade <= 14:
    print('o ateleta com idade de {} anos está na categoria INFANTIL. '.format(idade))
elif idade > 14 and idade <= 19:
    print('o ateleta com idade de {} anos está na categoria JUNIOR. '.format(idade))
elif idade == 20:
    print('o ateleta com idade de {} anos está na categoria SENIOR. '.format(idade))
else:
    idade > 19
    print('o ateleta com idade de {} anos está na categoria MASTER. '.format(idade))
