nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('o aluno está arpovado')
elif media >= 5 and media < 6.9:
    print('O aluno está de recuperação')
else:
    media < 5
    print('O aluno está reprovado')

