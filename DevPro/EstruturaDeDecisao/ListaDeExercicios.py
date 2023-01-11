# 3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Escreva qual é o seu sexo, masculino (m), feminio (f), outros (o): ').upper()
if sexo == 'M':
  print('Masculino')
elif sexo == 'F':
  print('Feminino')
elif sexo == 'O':
  print('Outro')
else:
  print('Sexo inválido')

print('Finalizou o programa')
