nome = str(input('Digite seu nome: ')).upper().strip()
if nome == 'PEDRO':
    print('que nome bonito!')
elif nome == 'BRENO' or nome == 'ANA' or nome == ('VITOR'):
    print('seu nome é bem popular no Brasil')
else:
    print('seu nome é incomum por aqui!')
print('tenha um bom dia {}!'.format(nome))
