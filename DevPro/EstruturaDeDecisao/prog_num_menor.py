# Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Escreva um número: '))
numero2 = int(input('Escreva outro número: '))
if numero1 > numero2:
    print(f'{numero1} é o maior número.')
elif numero1 < numero2:
    print(f'{numero2} é o maior número.')
else:
    print('Os números são iguais.')
