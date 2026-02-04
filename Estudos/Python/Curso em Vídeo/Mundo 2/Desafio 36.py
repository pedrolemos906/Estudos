#input
casavalor = float(input('qual o valor da casa? R$: '))
salario = float(input('qual o valor do seu salario? R$: '))
tempo = int(input('por quanto tempo voce vai pagar? '))


#calculos
prestacao = casavalor / (tempo * 12)
margem = salario * 0.30


#resultado
print('=-='*20)

if prestacao > margem:
    print('infelismente seu crétido não foi aprovado.')

else:
    prestacao <= margem
    print('seu credito foi aprovado!')
    print('O emprestimo será no valor de R${:.2f} e será parcelado em {} vezes de R${:.2f}. '.format(casavalor, tempo, prestacao))
