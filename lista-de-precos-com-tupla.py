listagem = ('Capinha', 15,
            'Fone', 10,
            'Mouse', 30,
            'Teclado', 80,
            'Controle de xbox', 150,
            'Controle de ps4', 200,
            'Cabo tipo c', 20,
            'Powerbank', 100,
            'Caixa de som', 100,)
print('=-'*20)
print(f'{"LISTA DE PREÇOS":^35}')
print('=-'*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:-<30}', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
