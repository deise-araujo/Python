
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num > 20:
        num = int(input('numero incorreto! \nDigite um numero entre 0 e 20: '))
    if num < 0:
        num = int(input('numero incorreto! \nDigite um numero entre 0 e 20: '))
    break
print(f'voce digitou o numero {numero[num]}')
