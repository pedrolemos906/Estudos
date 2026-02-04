nome = str(input('Digite seu nome completo: ')).strip()
print('esse é seu nome com todas as letras maiusculas:{}'.format(nome.upper()))
print('esse é seu nome com todas as letras minusculas:{}'.format(nome.lower()))
print('seu nome tem um total de {}.'.format(len(nome)-nome.count(' ')))

