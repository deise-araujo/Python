import random
dado = random.randint(0, 6)
jogo = str(input('Você gostaria de jogar o dado? [S/N]: ')).strip().upper()[0]
if jogo == 'S':
    print(f'O resutado do dado foi {dado}')
    jogador = 'S'
    while jogador == 'S':
        jogador = str(input('Deseja jogar novamente? ')).strip().upper()[0]
        if jogador == 'S':
            if jogador == 'S':
                dado = random.randint(0, 6)
                print(f'O resutado do dado foi {dado}')
        elif jogador == 'N':
            print('Obrigado por jogar!')
        else:
            print('erro tente novamente')
elif jogo == 'N':
    print('OK! Volte sempre!')

elif jogo != 'S' and 'N':
    print('invalido tente novamente')
    jogo = 'S'
    while jogo == 'S':
        jogador = str(input('Digite S para SIM e N para NAO!\n'
                            'Você gostaria de jogar o dado? [S/N]: ')).strip().upper()[0]
        if jogador == 'S':
            if jogador == 'S':
                dado = random.randint(0, 6)
                print(f'O resutado do dado foi {dado}')
        elif jogador == 'N':
            print('Obrigado por jogar!')
            break
        else:
            print('erro tente novamente')
