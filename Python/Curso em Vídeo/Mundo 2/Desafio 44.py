preco = float(input('informe o valor do produto: R$ '))

avista = preco - (preco * 0.10)
debito = preco - (preco * 0.05)
credito2x = preco
credito3x = preco + (preco * 0.20)

print('''selecione a forma de pagamento!
digite 1 para pagemento à vista no dinheiro/cheque.
digite 2 para pagemento à vista no cartao.
digite 3 para pagemento em até 2x no cartao.
digite 4 para pagemento em 3x ou mais no cartao.''')
opcao = int(input('informe a opcao: '))

if opcao == 1:
    print('O valor a ser pago é de R$ {:.2f}.'.format(avista))

elif opcao == 2:
    print('O valor a ser pago é de R$ {:.2f}.'.format(debito))

elif opcao == 3:
    print('O valor a ser pago é de R$ {:.2f}.'.format(credito2x))

elif opcao == 4:
    print('O valor a ser pago é de R$ {:.2f}.'.format(credito3x))

else:
    print('''opcao de pagamento invalida!
    tente novamente.''')