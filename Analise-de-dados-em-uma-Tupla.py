numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))

print(f'Você digitou os valores {numero}')
print(f'O valor 9 apreceu {numero.count(9)} vez(es).')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição.')
else:
    print('O número 3 nao apreceu em nenhuma posição.')

print('Os valores pares digitados foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
