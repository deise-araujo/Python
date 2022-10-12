#tupla com time de futebol

tabela = ('America-MG', 'Atletico-PR', 'Atletico-MG', 'Avai', 'Botafogo', 'Ceara SC', 'Corinthians'
          , 'Coritiba', 'Cuiaba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goias', 'Internacional',
          'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'Sao paulo')

print('=-' * 20)
print(f'Os 5 primeiro colocados sao {tabela[0:5]} ')
print(f'Os ultimos colocados sao {tabela[-4:]}')
print('=-' * 20)
print('os times da tabela em ordem alfabetica.\n', sorted(tabela))
print('=-' * 20)

time = str(input('digite o time para saber a sua posição: '))

if time in tabela:
    print(f'O {time} está na {tabela.index(time)+1}ª posição da tabela.')
else:
    print(f'O {time} não está na lista')
