import random
num = [random.randint(0, 9) for c in range(0, 4)]
print(f'os numeros sorteados foram: {num}')

print(f'O maior numero é {max(num)}\n'
      f'o menor numero é {min(num)}')
